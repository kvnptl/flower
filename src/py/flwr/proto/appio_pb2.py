# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flwr/proto/appio.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flwr.proto import fab_pb2 as flwr_dot_proto_dot_fab__pb2
from flwr.proto import run_pb2 as flwr_dot_proto_dot_run__pb2
from flwr.proto import transport_pb2 as flwr_dot_proto_dot_transport__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x66lwr/proto/appio.proto\x12\nflwr.proto\x1a\x14\x66lwr/proto/fab.proto\x1a\x14\x66lwr/proto/run.proto\x1a\x1a\x66lwr/proto/transport.proto\"+\n\x1aPullClientAppInputsRequest\x12\r\n\x05token\x18\x01 \x01(\x12\"\xa5\x01\n\x1bPullClientAppInputsResponse\x12$\n\x07message\x18\x01 \x01(\x0b\x32\x13.flwr.proto.Message\x12$\n\x07\x63ontext\x18\x02 \x01(\x0b\x32\x13.flwr.proto.Context\x12\x1c\n\x03\x66\x61\x62\x18\x03 \x01(\x0b\x32\x0f.flwr.proto.Fab\x12\x1c\n\x03run\x18\x04 \x01(\x0b\x32\x0f.flwr.proto.Run\"x\n\x1bPushClientAppOutputsRequest\x12\r\n\x05token\x18\x01 \x01(\x12\x12$\n\x07message\x18\x02 \x01(\x0b\x32\x13.flwr.proto.Message\x12$\n\x07\x63ontext\x18\x03 \x01(\x0b\x32\x13.flwr.proto.Context\"B\n\x1cPushClientAppOutputsResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.flwr.proto.Status2\xe4\x01\n\x0b\x43lientAppIo\x12h\n\x13PullClientAppInputs\x12&.flwr.proto.PullClientAppInputsRequest\x1a\'.flwr.proto.PullClientAppInputsResponse\"\x00\x12k\n\x14PushClientAppOutputs\x12\'.flwr.proto.PushClientAppOutputsRequest\x1a(.flwr.proto.PushClientAppOutputsResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flwr.proto.appio_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PULLCLIENTAPPINPUTSREQUEST']._serialized_start=110
  _globals['_PULLCLIENTAPPINPUTSREQUEST']._serialized_end=153
  _globals['_PULLCLIENTAPPINPUTSRESPONSE']._serialized_start=156
  _globals['_PULLCLIENTAPPINPUTSRESPONSE']._serialized_end=321
  _globals['_PUSHCLIENTAPPOUTPUTSREQUEST']._serialized_start=323
  _globals['_PUSHCLIENTAPPOUTPUTSREQUEST']._serialized_end=443
  _globals['_PUSHCLIENTAPPOUTPUTSRESPONSE']._serialized_start=445
  _globals['_PUSHCLIENTAPPOUTPUTSRESPONSE']._serialized_end=511
  _globals['_CLIENTAPPIO']._serialized_start=514
  _globals['_CLIENTAPPIO']._serialized_end=742
# @@protoc_insertion_point(module_scope)
