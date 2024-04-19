# foxglove_msgs/msg/TextMarker
# A marker representing a text label

# Generated by https://github.com/foxglove/schemas

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float64
from ..geometry_msgs.Pose import Pose
from .Color import Color

@dataclass
class TextMarker(IdlStruct, typename='foxglove_msgs/TextMarker'):
    # Position of the center of the text box and orientation of the text. Identity orientation means the text is oriented in the xy-plane and flows from -x to +x.
    pose: Pose = Pose()

    # Whether the text should respect `pose.orientation` (false) or always face the camera (true)
    billboard: bool = False

    # Font size (height of one line of text)
    font_size: float64 = 0

    # Indicates whether `font_size` is a fixed size in screen pixels (true), or specified in world coordinates and scales with distance from the camera (false)
    scale_invariant: bool = False

    # Color of the text
    color: Color = Color()

    # Text
    text: str = ''
