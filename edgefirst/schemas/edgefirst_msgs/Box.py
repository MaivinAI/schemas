# Box Message Interface - edgefirst/Box
# The Box message has the box attributes

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float32
from .Track import Track

@dataclass
class Box(IdlStruct, typename='edgefirst_msgs/Box'):
    center_x: float32 =  0 # Normalized x-coordinate of the center
    center_y: float32 =  0 # Normalized y-coordinate of the center
    width: float32 =     0 # Normalized width of the box
    height: float32 =    0 # Normalized height of the box
    label: str =        '' # object label
    score: float32 =     0 # confidence score for detection
    distance: float32 =  0 # Distance of object (if known)
    speed: float32 =     0 # Speed of object (if known)
    track: Track = Track() # object tracking, each track includes ID and lifetime information