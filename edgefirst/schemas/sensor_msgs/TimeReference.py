# Measurement from an external time source not actively synchronized with the system clock.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from ..std_msgs.Header import Header
from ..builtin_interfaces.Time import Time

@dataclass
class TimeReference(IdlStruct, typename='sensor_msgs/TimeReference'):
    header: Header = Header() # stamp is system time for which measurement was valid
                              # frame_id is not used

time_ref: Time = Time()       # corresponding time from this external source
source: str = ''              # (optional) name of time source