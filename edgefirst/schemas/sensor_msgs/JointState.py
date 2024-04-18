# This is a message that holds data to describe the state of a set of torque controlled joints.
#
# The state of each joint (revolute or prismatic) is defined by:
#  * the position of the joint (rad or m),
#  * the velocity of the joint (rad/s or m/s) and
#  * the effort that is applied in the joint (Nm or N).
#
# Each joint is uniquely identified by its name
# The header specifies the time at which the joint states were recorded. All the joint states
# in one message have to be recorded at the same time.
#
# This message consists of a multiple arrays, one for each part of the joint state.
# The goal is to make each of the fields optional. When e.g. your joints have no
# effort associated with them, you can leave the effort array empty.
#
# All arrays in this message should have the same size, or be empty.
# This is the only way to uniquely associate the joint name with the correct
# states.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float64, sequence
from ..std_msgs.Header import Header
from .. import default_field

@dataclass
class JointState(IdlStruct, typename='sensor_msgs/JointState'):
    header: Header = Header()

    name: sequence[str] = default_field([])
    position: sequence[float64] = default_field([])
    velocity: sequence[float64] = default_field([])
    effort: sequence[float64] = default_field([])