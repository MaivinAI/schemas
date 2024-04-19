# This expresses an estimated pose with a reference coordinate frame and timestamp

from dataclasses import dataclass
from pycdr2 import IdlStruct
from ..std_msgs.Header import Header
from .PoseWithCovariance import PoseWithCovariance

@dataclass
class PoseWithCovarianceStamped(IdlStruct, typename='geometry_msgs/PoseWithCovarianceStamped'):
    header: Header = Header()
    pose: PoseWithCovariance = PoseWithCovariance()