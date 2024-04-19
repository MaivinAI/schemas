# This message publishes values for multiple feedback at once.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import sequence
from .JoyFeedback import JoyFeedback
from .. import default_field

@dataclass
class JoyFeedbackArray(IdlStruct, typename='sensor_msgs/JoyFeedbackArray'):
    array: sequence[JoyFeedback] = default_field([])