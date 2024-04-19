# This represents an orientation in free space in quaternion form.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float64

@dataclass
class Quaternion(IdlStruct, typename='geometry_msgs/Quaternion'):
    x: float64 = 0
    y: float64 = 0
    z: float64 = 0
    w: float64 = 1