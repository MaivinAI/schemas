from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float32

@dataclass
class ColorRGBA(IdlStruct, typename='std_msgs/ColorRGBA'):
    r: float32 = 0
    g: float32 = 0
    b: float32 = 0
    a: float32 = 0
