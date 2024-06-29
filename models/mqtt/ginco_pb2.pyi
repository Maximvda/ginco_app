from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InfoRequest(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VERSION: _ClassVar[InfoRequest]
    DEVICE_LIST: _ClassVar[InfoRequest]
VERSION: InfoRequest
DEVICE_LIST: InfoRequest

class Upgrade(_message.Message):
    __slots__ = ("device_id", "image_size")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    device_id: int
    image_size: int
    def __init__(self, device_id: _Optional[int] = ..., image_size: _Optional[int] = ...) -> None: ...

class ConfigureSensor(_message.Message):
    __slots__ = ("input_id", "is_button", "active_high", "initial_state")
    INPUT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_BUTTON_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_HIGH_FIELD_NUMBER: _ClassVar[int]
    INITIAL_STATE_FIELD_NUMBER: _ClassVar[int]
    input_id: int
    is_button: bool
    active_high: bool
    initial_state: bool
    def __init__(self, input_id: _Optional[int] = ..., is_button: bool = ..., active_high: bool = ..., initial_state: bool = ...) -> None: ...

class ConfigureActuator(_message.Message):
    __slots__ = ("output_id", "value", "is_pwm", "initial_value")
    OUTPUT_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    IS_PWM_FIELD_NUMBER: _ClassVar[int]
    INITIAL_VALUE_FIELD_NUMBER: _ClassVar[int]
    output_id: int
    value: int
    is_pwm: bool
    initial_value: int
    def __init__(self, output_id: _Optional[int] = ..., value: _Optional[int] = ..., is_pwm: bool = ..., initial_value: _Optional[int] = ...) -> None: ...

class Action(_message.Message):
    __slots__ = ("device_id", "actuator_id", "value")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    ACTUATOR_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    device_id: int
    actuator_id: int
    value: int
    def __init__(self, device_id: _Optional[int] = ..., actuator_id: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...

class ConfigureScene(_message.Message):
    __slots__ = ("actions",)
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedCompositeFieldContainer[Action]
    def __init__(self, actions: _Optional[_Iterable[_Union[Action, _Mapping]]] = ...) -> None: ...

class Command(_message.Message):
    __slots__ = ("upgrade", "configure_sensor", "configure_actuator", "configure_scene", "action", "execute_scene", "info_request")
    UPGRADE_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_SENSOR_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_ACTUATOR_FIELD_NUMBER: _ClassVar[int]
    CONFIGURE_SCENE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    EXECUTE_SCENE_FIELD_NUMBER: _ClassVar[int]
    INFO_REQUEST_FIELD_NUMBER: _ClassVar[int]
    upgrade: Upgrade
    configure_sensor: ConfigureSensor
    configure_actuator: ConfigureActuator
    configure_scene: ConfigureScene
    action: Action
    execute_scene: int
    info_request: InfoRequest
    def __init__(self, upgrade: _Optional[_Union[Upgrade, _Mapping]] = ..., configure_sensor: _Optional[_Union[ConfigureSensor, _Mapping]] = ..., configure_actuator: _Optional[_Union[ConfigureActuator, _Mapping]] = ..., configure_scene: _Optional[_Union[ConfigureScene, _Mapping]] = ..., action: _Optional[_Union[Action, _Mapping]] = ..., execute_scene: _Optional[int] = ..., info_request: _Optional[_Union[InfoRequest, str]] = ...) -> None: ...

class Device(_message.Message):
    __slots__ = ("id", "version_major", "version_minor")
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_MAJOR_FIELD_NUMBER: _ClassVar[int]
    VERSION_MINOR_FIELD_NUMBER: _ClassVar[int]
    id: int
    version_major: int
    version_minor: int
    def __init__(self, id: _Optional[int] = ..., version_major: _Optional[int] = ..., version_minor: _Optional[int] = ...) -> None: ...

class DeviceList(_message.Message):
    __slots__ = ("devices",)
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    devices: _containers.RepeatedCompositeFieldContainer[Device]
    def __init__(self, devices: _Optional[_Iterable[_Union[Device, _Mapping]]] = ...) -> None: ...

class Sensor(_message.Message):
    __slots__ = ("device_id", "sensor_id", "is_button")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    SENSOR_ID_FIELD_NUMBER: _ClassVar[int]
    IS_BUTTON_FIELD_NUMBER: _ClassVar[int]
    device_id: int
    sensor_id: int
    is_button: bool
    def __init__(self, device_id: _Optional[int] = ..., sensor_id: _Optional[int] = ..., is_button: bool = ...) -> None: ...

class SensorList(_message.Message):
    __slots__ = ("sensors",)
    SENSORS_FIELD_NUMBER: _ClassVar[int]
    sensors: _containers.RepeatedCompositeFieldContainer[Sensor]
    def __init__(self, sensors: _Optional[_Iterable[_Union[Sensor, _Mapping]]] = ...) -> None: ...

class Actuator(_message.Message):
    __slots__ = ("device_id", "actuator_id", "is_pwm")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    ACTUATOR_ID_FIELD_NUMBER: _ClassVar[int]
    IS_PWM_FIELD_NUMBER: _ClassVar[int]
    device_id: int
    actuator_id: int
    is_pwm: int
    def __init__(self, device_id: _Optional[int] = ..., actuator_id: _Optional[int] = ..., is_pwm: _Optional[int] = ...) -> None: ...

class ActuatorList(_message.Message):
    __slots__ = ("actuators",)
    ACTUATORS_FIELD_NUMBER: _ClassVar[int]
    actuators: _containers.RepeatedCompositeFieldContainer[Actuator]
    def __init__(self, actuators: _Optional[_Iterable[_Union[Actuator, _Mapping]]] = ...) -> None: ...

class Event(_message.Message):
    __slots__ = ("device_id", "sensor_id", "value")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    SENSOR_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    device_id: int
    sensor_id: int
    value: float
    def __init__(self, device_id: _Optional[int] = ..., sensor_id: _Optional[int] = ..., value: _Optional[float] = ...) -> None: ...

class InfoMessage(_message.Message):
    __slots__ = ("device_list", "sensor_list", "actuator_list", "event", "version")
    DEVICE_LIST_FIELD_NUMBER: _ClassVar[int]
    SENSOR_LIST_FIELD_NUMBER: _ClassVar[int]
    ACTUATOR_LIST_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    device_list: DeviceList
    sensor_list: SensorList
    actuator_list: ActuatorList
    event: Event
    version: Version
    def __init__(self, device_list: _Optional[_Union[DeviceList, _Mapping]] = ..., sensor_list: _Optional[_Union[SensorList, _Mapping]] = ..., actuator_list: _Optional[_Union[ActuatorList, _Mapping]] = ..., event: _Optional[_Union[Event, _Mapping]] = ..., version: _Optional[_Union[Version, _Mapping]] = ...) -> None: ...

class Version(_message.Message):
    __slots__ = ("major", "minor", "patch")
    MAJOR_FIELD_NUMBER: _ClassVar[int]
    MINOR_FIELD_NUMBER: _ClassVar[int]
    PATCH_FIELD_NUMBER: _ClassVar[int]
    major: int
    minor: int
    patch: int
    def __init__(self, major: _Optional[int] = ..., minor: _Optional[int] = ..., patch: _Optional[int] = ...) -> None: ...
