from dataclasses import dataclass
from .. import default_field
from ..std_msgs import Header
from ..builtin_interfaces import Time
from pycdr2 import IdlStruct
from pycdr2.types import float32, int32, sequence


@dataclass
class Track(IdlStruct, typename='Track'):
    id: str = '' # Unique identifier for the object track
    lifetime: int32 = 0 # Number of consecutive frames the object has been tracked
    created: Time = Time() # Time the track was first added

@dataclass
class Box(IdlStruct, typename='Box'):
    center_x: float32 = 0 # Normalized x-coordinate of the center
    center_y: float32 = 0 # Normalized y-coordinate of the center
    width: float32 = 0 # Normalized width of the box
    height: float32 = 0 # Normalized height of the box
    label: str = '' # object label
    score: float32 = 0 # confidence score for detection
    distance: float32 = 0 # Distance of object (if known)
    speed: float32 = 0 # Speed of object (if known)
    track: Track = Track() # object tracking, each track includes ID and lifetime information

@dataclass
class Detect(IdlStruct, typename='Detect'):
    header: Header = Header() # Metadata including timestamp and coordinate frame
    input_timestamp: Time = Time() # Timestamp of the input data (e.g., from camera)
    model_time: Time = Time() # Timestamp when the object was processed by the model
    output_time: Time = Time() # Timestamp when the processed output was available
    boxes: sequence[Box] = default_field([]) # Array of detected object bounding boxes

