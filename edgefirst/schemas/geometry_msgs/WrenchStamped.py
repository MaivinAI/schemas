# A wrench with reference coordinate frame and timestamp

from dataclasses import dataclass
from pycdr2 import IdlStruct
from ..std_msgs.Header import Header
from .Wrench import Wrench

@dataclass
class WrenchStamped(IdlStruct, typename='geometry_msgs/WrenchStamped'):
    header: Header = Header()
    wrench: Wrench = Wrench()