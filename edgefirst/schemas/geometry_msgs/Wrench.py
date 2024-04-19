# This represents force in free space, separated into its linear and angular parts.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from .Vector3 import Vector3

@dataclass
class Wrench(IdlStruct, typename='geometry_msgs/Wrench'):
    force: Vector3 = Vector3()
    torque: Vector3 = Vector3()