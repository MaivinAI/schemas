# This represents a Vector3 with reference coordinate frame and timestamp

# Note that this follows vector semantics with it always anchored at the origin,
# so the rotational elements of a transform are the only parts applied when transforming.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from ..std_msgs.Header import Header
from .Vector3 import Vector3

@dataclass
class Vector3Stamped(IdlStruct, typename='geometry_msgs/Vector3Stamped'):
    header: Header = Header()
    vector: Vector3 = Vector3()