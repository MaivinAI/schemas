# A specification of a polygon where the first and last points are assumed to be connected

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import sequence
from .Point32 import Point32
from .. import default_field

@dataclass
class Polygon(IdlStruct, typename='geometry_msgs/Polygon'):
    points: sequence[Point32] = default_field([])