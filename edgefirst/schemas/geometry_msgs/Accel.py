# This expresses acceleration in free space broken into its linear and angular parts.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from .Vector3 import Vector3

@dataclass
class Accel(IdlStruct, typename='geometry_msgs/Accel'):
    linear: Vector3 = Vector3()
    angular: Vector3 = Vector3()