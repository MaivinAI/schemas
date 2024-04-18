# This represents a Polygon with reference coordinate frame and timestamp

from dataclasses import dataclass
from pycdr2 import IdlStruct
from ..std_msgs.Header import Header
from .Polygon import Polygon

@dataclass
class PolygonStamped(IdlStruct, typename='geometry_msgs/PolygonStamped'):
    header: Header = Header()
    polygon: Polygon = Polygon()