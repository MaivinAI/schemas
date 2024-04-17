from dataclasses import dataclass, field
import copy
from pycdr2 import IdlStruct
from pycdr2.types import uint8, int32, uint32, sequence

def default_field(obj):
    return field(default_factory=lambda: copy.copy(obj))

@dataclass
class Time(IdlStruct, typename='Time'):
    sec: int32 = 0
    nanosec: uint32 = 0

@dataclass
class CompressedImage(IdlStruct, typename='CompressedImage'):
    timestamp: Time = Time()
    frame_id: str = ''
    data: sequence[uint8] = default_field([])
    format: str = ''

