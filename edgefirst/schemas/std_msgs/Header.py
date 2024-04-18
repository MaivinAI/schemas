# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data
# in a particular coordinate frame.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from ..builtin_interfaces.Time import Time

@dataclass
class Header(IdlStruct, typename='std_msgs/Header'):
    # Two-integer timestamp that is expressed as seconds and nanoseconds.
    stamp: Time = Time()
    # Transform frame with which this data is associated.
    frame_id: str = ''