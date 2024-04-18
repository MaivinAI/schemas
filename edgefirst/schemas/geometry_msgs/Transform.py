# This represents the transform between two coordinate frames in free space.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from .Vector3 import Vector3
from .Quaternion import Quaternion

@dataclass
class Transform(IdlStruct, typename='geometry_msgs/Transform'):
    translation: Vector3 = Vector3()
    rotation: Quaternion = Quaternion()