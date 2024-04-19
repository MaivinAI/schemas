# This contains the position of a point in free space(with 32 bits of precision).
# It is recommended to use Point wherever possible instead of Point32.
#
# This recommendation is to promote interoperability.
#
# This message is designed to take up less space when sending
# lots of points at once, as in the case of a PointCloud.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float32

@dataclass
class Point32(IdlStruct, typename='geometry_msgs/Point32'):
    x: float32 = 0
    y: float32 = 0
    z: float32 = 0