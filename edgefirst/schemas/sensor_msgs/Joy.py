# Reports the state of a joystick's axes and buttons.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float32, int32, sequence
from ..std_msgs.Header import Header
from .. import default_field

@dataclass
class Joy(IdlStruct, typename='sensor_msgs/Joy'):
    # The timestamp is the time at which data is received from the joystick.
    header: Header = Header()

    # The axes measurements from a joystick.
    axes: sequence[float32] = default_field([])

    # The buttons measurements from a joystick.
    buttons: sequence[int32] = default_field([])