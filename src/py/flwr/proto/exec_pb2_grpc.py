# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from flwr.proto import exec_pb2 as flwr_dot_proto_dot_exec__pb2


class ExecStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StartRun = channel.unary_unary(
                '/flwr.proto.Exec/StartRun',
                request_serializer=flwr_dot_proto_dot_exec__pb2.StartRunRequest.SerializeToString,
                response_deserializer=flwr_dot_proto_dot_exec__pb2.StartRunResponse.FromString,
                )
        self.StreamLogs = channel.unary_stream(
                '/flwr.proto.Exec/StreamLogs',
                request_serializer=flwr_dot_proto_dot_exec__pb2.StreamLogsRequest.SerializeToString,
                response_deserializer=flwr_dot_proto_dot_exec__pb2.StreamLogsResponse.FromString,
                )
        self.Login = channel.unary_unary(
                '/flwr.proto.Exec/Login',
                request_serializer=flwr_dot_proto_dot_exec__pb2.LoginRequest.SerializeToString,
                response_deserializer=flwr_dot_proto_dot_exec__pb2.LoginResponse.FromString,
                )


class ExecServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StartRun(self, request, context):
        """Start run upon request
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamLogs(self, request, context):
        """Start log stream upon request
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Login(self, request, context):
        """Start login upon request
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ExecServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StartRun': grpc.unary_unary_rpc_method_handler(
                    servicer.StartRun,
                    request_deserializer=flwr_dot_proto_dot_exec__pb2.StartRunRequest.FromString,
                    response_serializer=flwr_dot_proto_dot_exec__pb2.StartRunResponse.SerializeToString,
            ),
            'StreamLogs': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamLogs,
                    request_deserializer=flwr_dot_proto_dot_exec__pb2.StreamLogsRequest.FromString,
                    response_serializer=flwr_dot_proto_dot_exec__pb2.StreamLogsResponse.SerializeToString,
            ),
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=flwr_dot_proto_dot_exec__pb2.LoginRequest.FromString,
                    response_serializer=flwr_dot_proto_dot_exec__pb2.LoginResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'flwr.proto.Exec', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Exec(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StartRun(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flwr.proto.Exec/StartRun',
            flwr_dot_proto_dot_exec__pb2.StartRunRequest.SerializeToString,
            flwr_dot_proto_dot_exec__pb2.StartRunResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamLogs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/flwr.proto.Exec/StreamLogs',
            flwr_dot_proto_dot_exec__pb2.StreamLogsRequest.SerializeToString,
            flwr_dot_proto_dot_exec__pb2.StreamLogsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flwr.proto.Exec/Login',
            flwr_dot_proto_dot_exec__pb2.LoginRequest.SerializeToString,
            flwr_dot_proto_dot_exec__pb2.LoginResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
