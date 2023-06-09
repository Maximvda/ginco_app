# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ginco.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ginco.proto',
  package='ginco',
  syntax='proto3',
  serialized_pb=_b('\n\x0bginco.proto\x12\x05ginco\"0\n\x07Upgrade\x12\x11\n\tdevice_id\x18\x01 \x01(\r\x12\x12\n\nimage_size\x18\x02 \x01(\r\"7\n\x07\x43ommand\x12!\n\x07upgrade\x18\x01 \x01(\x0b\x32\x0e.ginco.UpgradeH\x00\x42\t\n\x07\x63ommand\",\n\x08\x43ommands\x12 \n\x08\x63ommands\x18\x01 \x03(\x0b\x32\x0e.ginco.Commandb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_UPGRADE = _descriptor.Descriptor(
  name='Upgrade',
  full_name='ginco.Upgrade',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_id', full_name='ginco.Upgrade.device_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='image_size', full_name='ginco.Upgrade.image_size', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=70,
)


_COMMAND = _descriptor.Descriptor(
  name='Command',
  full_name='ginco.Command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='upgrade', full_name='ginco.Command.upgrade', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='command', full_name='ginco.Command.command',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=72,
  serialized_end=127,
)


_COMMANDS = _descriptor.Descriptor(
  name='Commands',
  full_name='ginco.Commands',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='commands', full_name='ginco.Commands.commands', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=173,
)

_COMMAND.fields_by_name['upgrade'].message_type = _UPGRADE
_COMMAND.oneofs_by_name['command'].fields.append(
  _COMMAND.fields_by_name['upgrade'])
_COMMAND.fields_by_name['upgrade'].containing_oneof = _COMMAND.oneofs_by_name['command']
_COMMANDS.fields_by_name['commands'].message_type = _COMMAND
DESCRIPTOR.message_types_by_name['Upgrade'] = _UPGRADE
DESCRIPTOR.message_types_by_name['Command'] = _COMMAND
DESCRIPTOR.message_types_by_name['Commands'] = _COMMANDS

Upgrade = _reflection.GeneratedProtocolMessageType('Upgrade', (_message.Message,), dict(
  DESCRIPTOR = _UPGRADE,
  __module__ = 'ginco_pb2'
  # @@protoc_insertion_point(class_scope:ginco.Upgrade)
  ))
_sym_db.RegisterMessage(Upgrade)

Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), dict(
  DESCRIPTOR = _COMMAND,
  __module__ = 'ginco_pb2'
  # @@protoc_insertion_point(class_scope:ginco.Command)
  ))
_sym_db.RegisterMessage(Command)

Commands = _reflection.GeneratedProtocolMessageType('Commands', (_message.Message,), dict(
  DESCRIPTOR = _COMMANDS,
  __module__ = 'ginco_pb2'
  # @@protoc_insertion_point(class_scope:ginco.Commands)
  ))
_sym_db.RegisterMessage(Commands)


# @@protoc_insertion_point(module_scope)
