# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/extensions/quic/server_preferred_address/v3/fixed_server_preferred_address_config.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from xds.annotations.v3 import status_pb2 as xds_dot_annotations_dot_v3_dot_status__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n]envoy/extensions/quic/server_preferred_address/v3/fixed_server_preferred_address_config.proto\x12\x31\x65nvoy.extensions.quic.server_preferred_address.v3\x1a\x1fxds/annotations/v3/status.proto\x1a\x1dudpa/annotations/status.proto\"w\n!FixedServerPreferredAddressConfig\x12\x16\n\x0cipv4_address\x18\x01 \x01(\tH\x00\x12\x16\n\x0cipv6_address\x18\x02 \x01(\tH\x01:\x08\xd2\xc6\xa4\xe1\x06\x02\x08\x01\x42\x0b\n\tipv4_typeB\x0b\n\tipv6_typeB\xe8\x01\n?io.envoyproxy.envoy.extensions.quic.server_preferred_address.v3B&FixedServerPreferredAddressConfigProtoP\x01Zsgithub.com/envoyproxy/go-control-plane/envoy/extensions/quic/server_preferred_address/v3;server_preferred_addressv3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'envoy.extensions.quic.server_preferred_address.v3.fixed_server_preferred_address_config_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n?io.envoyproxy.envoy.extensions.quic.server_preferred_address.v3B&FixedServerPreferredAddressConfigProtoP\001Zsgithub.com/envoyproxy/go-control-plane/envoy/extensions/quic/server_preferred_address/v3;server_preferred_addressv3\272\200\310\321\006\002\020\002'
  _globals['_FIXEDSERVERPREFERREDADDRESSCONFIG']._options = None
  _globals['_FIXEDSERVERPREFERREDADDRESSCONFIG']._serialized_options = b'\322\306\244\341\006\002\010\001'
  _globals['_FIXEDSERVERPREFERREDADDRESSCONFIG']._serialized_start=212
  _globals['_FIXEDSERVERPREFERREDADDRESSCONFIG']._serialized_end=331
# @@protoc_insertion_point(module_scope)