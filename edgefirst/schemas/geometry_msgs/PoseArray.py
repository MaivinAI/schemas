# An array of poses with a header for global reference.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import sequence
from ..std_msgs.Header import Header
from .Pose import Pose
from .. import default_field

@dataclass
class PoseArray(IdlStruct, typename='geometry_msgs/PoseArray'):
    header: Header = Header()

    poses: sequence[Pose] = default_field([])