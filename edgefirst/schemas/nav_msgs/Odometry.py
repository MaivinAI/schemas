# This represents an estimate of a position and velocity in free space.
# The pose in this message should be specified in the coordinate frame given by header.frame_id
# The twist in this message should be specified in the coordinate frame given by the child_frame_id

from dataclasses import dataclass
from pycdr2 import IdlStruct
from ..std_msgs.Header import Header
from ..geometry_msgs.PoseWithCovariance import PoseWithCovariance
from ..geometry_msgs.TwistWithCovariance import TwistWithCovariance

@dataclass
class Odometry(IdlStruct, typename='nav_msgs/Odometry'):
    # Includes the frame id of the pose parent.
    header: Header = Header()

    # Frame id the pose points to. The twist is in this coordinate frame.
    child_frame_id: str = ''

    # Estimated pose that is typically relative to a fixed world frame.
    pose: PoseWithCovariance = PoseWithCovariance()

    # Estimated linear and angular velocity relative to child_frame_id.
    twist: TwistWithCovariance = TwistWithCovariance()