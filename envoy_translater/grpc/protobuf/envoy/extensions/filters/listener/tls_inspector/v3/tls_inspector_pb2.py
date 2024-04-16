# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/extensions/filters/listener/tls_inspector/v3/tls_inspector.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nFenvoy/extensions/filters/listener/tls_inspector/v3/tls_inspector.proto\x12\x32\x65nvoy.extensions.filters.listener.tls_inspector.v3\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\x1a\x17validate/validate.proto\"\xde\x01\n\x0cTlsInspector\x12=\n\x19\x65nable_ja3_fingerprinting\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12L\n\x18initial_read_buffer_size\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueB\x0c\xfa\x42\t*\x07\x10\x81\x80\x04 \xff\x01:A\x9a\xc5\x88\x1e<\n:envoy.config.filter.listener.tls_inspector.v2.TlsInspectorB\xca\x01\n@io.envoyproxy.envoy.extensions.filters.listener.tls_inspector.v3B\x11TlsInspectorProtoP\x01Zigithub.com/envoyproxy/go-control-plane/envoy/extensions/filters/listener/tls_inspector/v3;tls_inspectorv3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'envoy.extensions.filters.listener.tls_inspector.v3.tls_inspector_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n@io.envoyproxy.envoy.extensions.filters.listener.tls_inspector.v3B\021TlsInspectorProtoP\001Zigithub.com/envoyproxy/go-control-plane/envoy/extensions/filters/listener/tls_inspector/v3;tls_inspectorv3\272\200\310\321\006\002\020\002'
  _globals['_TLSINSPECTOR'].fields_by_name['initial_read_buffer_size']._options = None
  _globals['_TLSINSPECTOR'].fields_by_name['initial_read_buffer_size']._serialized_options = b'\372B\t*\007\020\201\200\004 \377\001'
  _globals['_TLSINSPECTOR']._options = None
  _globals['_TLSINSPECTOR']._serialized_options = b'\232\305\210\036<\n:envoy.config.filter.listener.tls_inspector.v2.TlsInspector'
  _globals['_TLSINSPECTOR']._serialized_start=250
  _globals['_TLSINSPECTOR']._serialized_end=472
# @@protoc_insertion_point(module_scope)
