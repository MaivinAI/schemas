# A representation of pose in free space, composed of position and orientation.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from .Point import Point
from .Quaternion import Quaternion

@dataclass
class Pose(IdlStruct, typename='geometry_msgs/Pose'):
    position: Point = Point()
    orientation: Quaternion = Quaternion()