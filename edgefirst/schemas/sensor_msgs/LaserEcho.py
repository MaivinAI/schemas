# This message is a submessage of MultiEchoLaserScan and is not intended
# to be used separately.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float32, sequence
from .. import default_field

@dataclass
class LaserEcho(IdlStruct, typename='sensor_msgs/LaserEcho'):
    echoes: sequence[float32] = default_field([])  # Multiple values of ranges or intensities.
                                                   # Each array represents data from the same angle increment.