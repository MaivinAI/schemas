# An accel with reference coordinate frame and timestamp

from dataclasses import dataclass
from pycdr2 import IdlStruct
from ..std_msgs.Header import Header
from .Accel import Accel

@dataclass
class AccelStamped(IdlStruct, typename='geometry_msgs/AccelStamped'):
    header: Header = Header()
    accel: Accel = Accel()