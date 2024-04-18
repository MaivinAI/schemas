from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float32, uint8
from enum import Enum

class FeedbackType(Enum):
    TYPE_LED    = 0
    TYPE_RUMBLE = 1
    TYPE_BUZZER = 2

@dataclass
class JoyFeedback(IdlStruct, typename='sensor_msgs/JoyFeedback'):
    # Declare of the type of feedback
    type: uint8 = 0

    # This will hold an id number for each type of each feedback.
    # Example, the first led would be id=0, the second would be id=1
    id: uint8 = 0

    # Intensity of the feedback, from 0.0 to 1.0, inclusive.  If device is
    # actually binary, driver should treat 0<=x<0.5 as off, 0.5<=x<=1 as on.
    intensity: float32 = 0