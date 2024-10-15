# Copyright 2021 Flower Labs GmbH. All Rights Reserved.
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
"""FedAdagrad tests."""


from unittest.mock import MagicMock

from numpy import array, float32

from flwr.common import (
    Code,
    FitRes,
    NDArrays,
    Parameters,
    Status,
    ndarrays_to_parameters,
    parameters_to_ndarrays,
)
from flwr.server.client_proxy import ClientProxy
from flwr.server.superlink.fleet.grpc_bidi.grpc_client_proxy import GrpcClientProxy

from .fedadagrad import FedAdagrad


def test_aggregate_fit() -> None:
    """Tests if adagrad function is aggregating correctly."""
    # Prepare
    previous_weights: NDArrays = [array([0.1, 0.1, 0.1, 0.1], dtype=float32)]
    strategy = FedAdagrad(
        eta=0.1,
        eta_l=0.316,
        tau=0.5,
        initial_parameters=ndarrays_to_parameters(previous_weights),
    )
    param_0: Parameters = ndarrays_to_parameters(
        [array([0.2, 0.2, 0.2, 0.2], dtype=float32)]
    )
    param_1: Parameters = ndarrays_to_parameters(
        [array([1.0, 1.0, 1.0, 1.0], dtype=float32)]
    )
    bridge = MagicMock()
    client_0 = GrpcClientProxy(cid="0", bridge=bridge)
    client_1 = GrpcClientProxy(cid="1", bridge=bridge)
    results: list[tuple[ClientProxy, FitRes]] = [
        (
            client_0,
            FitRes(
                status=Status(code=Code.OK, message="Success"),
                parameters=param_0,
                num_examples=5,
                metrics={},
            ),
        ),
        (
            client_1,
            FitRes(
                status=Status(code=Code.OK, message="Success"),
                parameters=param_1,
                num_examples=5,
                metrics={},
            ),
        ),
    ]
    expected: NDArrays = [array([0.15, 0.15, 0.15, 0.15], dtype=float32)]

    # Execute
    actual_aggregated, _ = strategy.aggregate_fit(
        server_round=1, results=results, failures=[]
    )
    assert actual_aggregated
    actual_list = parameters_to_ndarrays(actual_aggregated)
    actual = actual_list[0]
    assert (actual == expected[0]).all()
