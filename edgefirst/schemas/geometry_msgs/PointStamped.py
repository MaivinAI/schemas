# This represents a Point with reference coordinate frame and timestamp

from dataclasses import dataclass
from pycdr2 import IdlStruct
from ..std_msgs.Header import Header
from .Point import Point

@dataclass
class PointStamped(IdlStruct, typename='geometry_msgs/PointStamped'):
    header: Header = Header()
    point: Point = Point()