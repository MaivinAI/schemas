# Detect Message Interface - edgefirst/detect/boxes2d
#
# The detect interface carries detection information 

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import sequence
from ..builtin_interfaces.Time import Time
from ..std_msgs.Header import Header
from .Box import Box
from .. import default_field

@dataclass
class Detect(IdlStruct, typename='edgefirst_msgs/Detect'):
    header: Header =      Header() # Metadata including timestamp and coordinate frame

    input_timestamp: Time = Time() # Timestamp of the input data (e.g., from camera)
    model_time: Time =      Time() # Inference duration for the model to process the image
    output_time: Time =     Time() # Timestamp when the message was sent out

    boxes: sequence[Box] = default_field([]) # Array of detected object bounding boxes
                                             # Each box includes normalized center point, width, and height