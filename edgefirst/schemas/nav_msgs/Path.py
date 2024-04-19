# An array of poses that represents a Path for a robot to follow.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import sequence
from ..std_msgs.Header import Header
from ..geometry_msgs.PoseStamped import PoseStamped
from .. import default_field

@dataclass
class Path(IdlStruct, typename='nav_msgs/Path'):
    # Indicates the frame_id of the path.
    header: Header = Header()

    # Array of poses to follow.
    poses: sequence[PoseStamped] = default_field([])