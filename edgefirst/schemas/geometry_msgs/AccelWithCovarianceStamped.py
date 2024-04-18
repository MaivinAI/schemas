# This represents an estimated accel with reference coordinate frame and timestamp.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from ..std_msgs.Header import Header
from .AccelWithCovariance import AccelWithCovariance

@dataclass
class AccelWithCovarianceStamped(IdlStruct, typename='geometry_msgs/AccelWithCovarianceStamped'):
    header: Header = Header()
    accel: AccelWithCovariance = AccelWithCovariance()