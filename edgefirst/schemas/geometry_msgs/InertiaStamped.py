# An Inertia with a time stamp and reference frame.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from ..std_msgs.Header import Header
from .Inertia import Inertia

@dataclass
class InertiaStamped(IdlStruct, typename='geometry_msgs/InertiaStamped'):
    header: Header = Header()
    inertia: Inertia = Inertia()