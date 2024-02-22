# Copyright 2024 Flower Labs GmbH. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Ray backend for the Fleet API using the VCE."""

import asyncio
import pathlib
from logging import INFO
from typing import Callable, Dict, List, Tuple, Union

from flwr.client.clientapp import ClientApp
from flwr.common.context import Context
from flwr.common.logger import log
from flwr.common.message import Message
from flwr.simulation.ray_transport.ray_actor import (
    BasicActorPool,
    ClientAppActor,
    init_ray,
)

from .backend import Backend, BackendConfig

ClienteResourcesDict = Dict[str, Union[int, float]]


class RayBackend(Backend):
    """A backend that submits jobs to a `BasicActorPool`."""

    def __init__(
        self,
        backend_config: BackendConfig,
        work_dir: str,
    ) -> None:
        """Prepare RayBackend by initialising Ray and creating the ActorPool."""
        log(INFO, "Backend config: %s", backend_config)

        # Init ray and append working dir if needed
        runtime_env = (
            self._configure_runtime_env(work_dir=work_dir) if work_dir else None
        )
        init_ray(runtime_env=runtime_env)

        # Validate client resources
        self.client_resources_key = "client_resources"

        # Create actor pool
        client_resources = self._validate_client_resources(config=backend_config)
        self.pool = BasicActorPool(
            actor_type=ClientAppActor,
            client_resources=client_resources,
        )

    def _configure_runtime_env(self, work_dir: str) -> Dict[str, Union[str, List[str]]]:
        """Return list of files/subdirectories to exclude relateive to work_dir.

        Without this, Ray will push everything to the Ray Cluster.
        """
        runtime_env: Dict[str, Union[str, List[str]]] = {"working_dir": work_dir}

        if runtime_env:
            excludes = []
            path = pathlib.Path(work_dir)
            for p in path.rglob("*"):
                # exclude files need to be relative to the working_dir
                if p.is_file() and not str(p).endswith('.py'):
                    excludes.append(str(p.relative_to(path)))
            runtime_env["excludes"] = excludes

        return runtime_env

    def _validate_client_resources(self, config: BackendConfig) -> ClienteResourcesDict:
        client_resources_config = config.get(self.client_resources_key)
        client_resources: ClienteResourcesDict = {}
        valid_types = (int, float)
        if client_resources_config:
            for k, v in client_resources_config.items():
                assert isinstance(k, str), ValueError(
                    f"client resources keys are expected to be `str` but you used "
                    f"{type(k)} for `{k}`"
                )
                assert isinstance(v, valid_types), ValueError(
                    f"client resources are expected to be of type {valid_types} but "
                    f"found `{type(v)}` for key `{k}`",
                )
                client_resources[k] = v

        else:
            client_resources = {"num_cpus": 2, "num_gpus": 0.0}
            log(
                INFO,
                "`%s` not specified in backend config. Applying default setting: %s",
                self.client_resources_key,
                client_resources,
            )

        return client_resources

    @property
    def num_workers(self) -> int:
        """Return number of actors in pool."""
        return self.pool.num_actors

    def is_worker_idle(self) -> bool:
        """Report whether the pool has idle actors."""
        return self.pool.is_actor_available()

    async def build(self) -> None:
        """Build pool of Ray actors that this backend will submit jobs to."""
        await self.pool.add_actors_to_pool(self.pool.actors_capacity)
        log(INFO, "Constructed ActorPool with: %i actors", self.pool.num_actors)

    async def process_message(
        self,
        app: Callable[[], ClientApp],
        message: Message,
        context: Context,
    ) -> Tuple[Message, Context]:
        """Run ClientApp that process a given message.

        Return output message and updated context.
        """
        node_id = message.metadata.dst_node_id

        # Submite a task to the pool
        future = await self.pool.submit(
            lambda a, a_fn, mssg, cid, state: a.run.remote(a_fn, mssg, cid, state),
            (app, message, str(node_id), context),
        )

        await asyncio.wait([future])

        # Fetch result
        (
            out_mssg,
            updated_context,
        ) = await self.pool.fetch_result_and_return_actor_to_pool(future)

        return out_mssg, updated_context
