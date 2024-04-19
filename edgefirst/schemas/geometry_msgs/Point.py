# This contains the position of a point in free space

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float64

@dataclass
class Point(IdlStruct, typename='geometry_msgs/Point'):
    x: float64 = 0
    y: float64 = 0
    z: float64 = 0