# foxglove_msgs/msg/LinePrimitive
# A primitive representing a series of points connected by lines

# Generated by https://github.com/foxglove/schemas

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import uint8, uint32, float64, sequence, array
from ..geometry_msgs.Pose import Pose
from ..geometry_msgs.Point import Point
from .Color import Color
from .. import default_field
from enum import Enum

class LinePrimitiveType(Enum):
    # Connected line segments: 0-1, 1-2, ..., (n-1)-n
    LINE_STRIP=0
    # Closed polygon: 0-1, 1-2, ..., (n-1)-n, n-0
    LINE_LOOP=1
    # Individual line segments: 0-1, 2-3, 4-5, ...
    LINE_LIST=2

@dataclass
class LinePrimitive(IdlStruct, typename='foxglove_msgs/LinePrimitive'):
    # Drawing primitive to use for lines
    type: uint8 = 0

    # Origin of lines relative to reference frame
    pose: Pose = Pose()

    # Line thickness
    thickness: float64 = 0

    # Indicates whether `thickness` is a fixed size in screen pixels (true), or specified in world coordinates and scales with distance from the camera (false)
    scale_invariant: bool = False

    # Points along the line
    points: sequence[Point] = default_field([])

    # Solid color to use for the whole line. One of `color` or `colors` must be provided.
    color: Color = Color()

    # Per-point colors (if specified, must have the same length as `points`). One of `color` or `colors` must be provided.
    colors: sequence[Color] = default_field([])

    # Indices into the `points` and `colors` attribute arrays, which can be used to avoid duplicating attribute data.
    # 
    # If omitted or empty, indexing will not be used. This default behavior is equivalent to specifying [0, 1, ..., N-1] for the indices (where N is the number of `points` provided).
    indices: sequence[uint32] = default_field([])
