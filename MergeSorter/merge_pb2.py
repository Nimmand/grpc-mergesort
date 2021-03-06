# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: merge.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='merge.proto',
  package='merge',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bmerge.proto\x12\x05merge\"\x1f\n\x0cMergeRequest\x12\x0f\n\x07numbers\x18\x01 \x03(\x05\"\x1d\n\nMergeReply\x12\x0f\n\x07numbers\x18\x01 \x03(\x05\x32>\n\x0bMergesorter\x12/\n\x05Merge\x12\x13.merge.MergeRequest\x1a\x11.merge.MergeReplyb\x06proto3'
)




_MERGEREQUEST = _descriptor.Descriptor(
  name='MergeRequest',
  full_name='merge.MergeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='numbers', full_name='merge.MergeRequest.numbers', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=53,
)


_MERGEREPLY = _descriptor.Descriptor(
  name='MergeReply',
  full_name='merge.MergeReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='numbers', full_name='merge.MergeReply.numbers', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=84,
)

DESCRIPTOR.message_types_by_name['MergeRequest'] = _MERGEREQUEST
DESCRIPTOR.message_types_by_name['MergeReply'] = _MERGEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MergeRequest = _reflection.GeneratedProtocolMessageType('MergeRequest', (_message.Message,), {
  'DESCRIPTOR' : _MERGEREQUEST,
  '__module__' : 'merge_pb2'
  # @@protoc_insertion_point(class_scope:merge.MergeRequest)
  })
_sym_db.RegisterMessage(MergeRequest)

MergeReply = _reflection.GeneratedProtocolMessageType('MergeReply', (_message.Message,), {
  'DESCRIPTOR' : _MERGEREPLY,
  '__module__' : 'merge_pb2'
  # @@protoc_insertion_point(class_scope:merge.MergeReply)
  })
_sym_db.RegisterMessage(MergeReply)



_MERGESORTER = _descriptor.ServiceDescriptor(
  name='Mergesorter',
  full_name='merge.Mergesorter',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=86,
  serialized_end=148,
  methods=[
  _descriptor.MethodDescriptor(
    name='Merge',
    full_name='merge.Mergesorter.Merge',
    index=0,
    containing_service=None,
    input_type=_MERGEREQUEST,
    output_type=_MERGEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MERGESORTER)

DESCRIPTOR.services_by_name['Mergesorter'] = _MERGESORTER

# @@protoc_insertion_point(module_scope)
