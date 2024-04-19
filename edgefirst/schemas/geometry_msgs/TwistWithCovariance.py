# This expresses velocity in free space with uncertainty.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float64, array
from .Twist import Twist
from .. import default_field

@dataclass
class TwistWithCovariance(IdlStruct, typename='geometry_msgs/TwistWithCovariance'):
    twist: Twist = Twist()

    # Row-major representation of the 6x6 covariance matrix
    # The orientation parameters use a fixed-axis representation.
    # In order, the parameters are:
    # (x, y, z, rotation about X axis, rotation about Y axis, rotation about Z axis)
    covariance: array[float64, 36] = default_field([0] * 36)