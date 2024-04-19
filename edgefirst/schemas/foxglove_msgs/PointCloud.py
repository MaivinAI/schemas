# foxglove_msgs/msg/PointCloud
# A collection of N-dimensional points, which may contain additional fields with information like normals, intensity, etc.

# Generated by https://github.com/foxglove/schemas

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import uint32, uint8, sequence
from ..builtin_interfaces.Time import Time
from ..geometry_msgs.Pose import Pose
from .PackedElementField import PackedElementField
from .. import default_field

@dataclass
class PointCloud(IdlStruct, typename='foxglove_msgs/PointCloud'):
    # Timestamp of point cloud
    timestamp: Time = Time()

    # Frame of reference
    frame_id: str = ''

    # The origin of the point cloud relative to the frame of reference
    pose: Pose = Pose()

    # Number of bytes between points in the `data`
    point_stride: uint32 = 0

    # Fields in `data`. At least 2 coordinate fields from `x`, `y`, and `z` are required for each point's position; `red`, `green`, `blue`, and `alpha` are optional for customizing each point's color.
    fields: sequence[PackedElementField] = default_field([])

    # Point data, interpreted using `fields`
    data: sequence[uint8] = default_field([])
