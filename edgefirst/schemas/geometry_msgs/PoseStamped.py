# A Pose with reference coordinate frame and timestamp

from dataclasses import dataclass
from pycdr2 import IdlStruct
from ..std_msgs.Header import Header
from .Pose import Pose

@dataclass
class PoseStamped(IdlStruct, typename='geometry_msgs/PoseStamped'):
    header: Header = Header()
    pose: Pose = Pose()