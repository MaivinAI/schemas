# Generated from Transform by @foxglove/schemas

from dataclasses import dataclass
from pycdr2 import IdlStruct
from ..builtin_interfaces.Time import Time
from ..geometry_msgs.Vector3 import Vector3
from ..geometry_msgs.Quaternion import Quaternion

@dataclass
class Transform(IdlStruct, typename='foxglove_msgs/Transform'):
    # Transform time
    timestamp: Time = Time()

    # Translation component of the transform
    translation: Vector3 = Vector3()

    # Rotation component of the transform
    rotation: Quaternion = Quaternion()
