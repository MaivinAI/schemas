# foxglove_msgs/msg/CircleAnnotation
# A circle annotation on a 2D image

# Generated by https://github.com/foxglove/schemas

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float64
from ..builtin_interfaces.Time import Time
from .Point2 import Point2
from .Color import Color

@dataclass
class CircleAnnotation(IdlStruct, typename='foxglove_msgs/CircleAnnotation'):
    # Timestamp of circle
    timestamp: Time = Time()

    # Center of the circle in 2D image coordinates (pixels)
    position: Point2 = Point2()

    # Circle diameter in pixels
    diameter: float64 = 0

    # Line thickness in pixels
    thickness: float64 = 0

    # Fill color
    fill_color: Color = Color()

    # Outline color
    outline_color: Color = Color()