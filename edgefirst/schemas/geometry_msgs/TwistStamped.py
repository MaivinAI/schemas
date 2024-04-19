# A twist with reference coordinate frame and timestamp

from dataclasses import dataclass
from pycdr2 import IdlStruct
from ..std_msgs.Header import Header
from .Twist import Twist

@dataclass
class TwistStamped(IdlStruct, typename='geometry_msgs/TwistStamped'):
    header: Header = Header()
    twist: Twist = Twist()