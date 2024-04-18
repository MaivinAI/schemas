# This represents an estimated twist with reference coordinate frame and timestamp.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from ..std_msgs.Header import Header
from .TwistWithCovariance import TwistWithCovariance

@dataclass
class TwistWithCovarianceStamped(IdlStruct, typename='geometry_msgs/TwistWithCovarianceStamped'):
    header: Header = Header()
    twist: TwistWithCovariance = TwistWithCovariance()