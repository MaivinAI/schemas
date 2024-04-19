# foxglove_msgs/msg/CylinderMarker
# A marker representing a cylinder or elliptic cylinder

# Generated by https://github.com/foxglove/schemas

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float64, sequence
from ..builtin_interfaces.Time import Time
from ..builtin_interfaces.Duration import Duration
from .KeyValuePair import KeyValuePair
from ..geometry_msgs.Pose import Pose
from .Color import Color
from .. import default_field

@dataclass
class CylinderMarker(IdlStruct, typename='foxglove_msgs/CylinderMarker'):
    # Timestamp of the marker
    timestamp: Time = Time()

    # Frame of reference
    frame_id: str = ''

    # Identifier for the marker. A marker will replace any prior marker on the same topic with the same `id`.
    id: str = ''

    # Length of time (relative to `timestamp`) after which the marker should be automatically removed. Zero value indicates the marker should remain visible until it is replaced or deleted.
    lifetime: Duration = Duration()

    # Whether the marker should keep its location in the fixed frame (false) or follow the frame specified in `frame_id` as it moves relative to the fixed frame (true)
    frame_locked: bool = False

    # Additional user-provided metadata associated with the marker. Keys must be unique.
    metadata: sequence[KeyValuePair] = default_field([])

    # Position of the center of the cylinder and orientation of the cylinder. The cylinder's flat faces are perpendicular to the z-axis.
    pose: Pose = Pose()

    # Radius of the cylinder at min z
    bottom_radius: float64 = 0

    # Radius of the cylinder at max z
    top_radius: float64 = 0

    # Height of the cylinder along the z axis
    height: float64 = 0

    # Color of the sphere
    color: Color = Color()