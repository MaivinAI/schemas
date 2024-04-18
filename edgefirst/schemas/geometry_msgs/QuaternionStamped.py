# This represents an orientation with reference coordinate frame and timestamp.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from ..std_msgs.Header import Header
from .Quaternion import Quaternion

@dataclass
class QuaternionStamped(IdlStruct, typename='geometry_msgs/QuaternionStamped'):
    header: Header = Header()
    quaternion: Quaternion = Quaternion()