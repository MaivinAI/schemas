from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import uint32, int32


@dataclass
class Time(IdlStruct, typename='Time'):
    sec: int32 = 0
    nanosec: uint32 = 0


@dataclass
class Duration(IdlStruct, typename='Duration'):
    sec: int32 = 0
    nanosec: uint32 = 0
