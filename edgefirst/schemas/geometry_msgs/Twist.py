# This expresses velocity in free space broken into its linear and angular parts.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from .Vector3 import Vector3

@dataclass
class Twist(IdlStruct, typename='geometry_msgs/Twist'):
    linear: Vector3 = Vector3()
    angular: Vector3 = Vector3()