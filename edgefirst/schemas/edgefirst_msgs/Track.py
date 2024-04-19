# Track Message Interface - edgefirst/Track
#
# The Track message has the track attributes

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import int32
from ..builtin_interfaces.Time import Time

@dataclass
class Track(IdlStruct, typename='edgefirst_msgs/Track'):
    id: str = '' # Unique identifier for the object track (if the object is not tracked then "")
    lifetime: int32 = 0 # Number of consecutive frames the object has been tracked
    created: Time = Time() # Time the track was first added