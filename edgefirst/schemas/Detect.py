from dataclasses import dataclass, field
import copy
from pycdr2 import IdlStruct
from pycdr2.types import float32, int32, uint32, sequence

def default_field(obj):
    return field(default_factory=lambda: copy.copy(obj))

@dataclass
class Time(IdlStruct, typename='Time'):
    sec: int32 = 0
    nanosec: uint32 = 0

@dataclass
class Track(IdlStruct, typename='Track'):
    id: str = '' # Unique identifier for the object track
    lifetime: int32 = 0 # Number of consecutive frames the object has been tracked
    created: Time = Time() # Time the track was first added

@dataclass
class Header(IdlStruct, typename='Header'):
    stamp: Time = Time()
    frame_id: str = ''

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

