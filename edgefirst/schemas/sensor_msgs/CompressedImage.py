# This message contains a compressed image.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import uint8, sequence
from ..std_msgs.Header import Header
from .. import default_field

@dataclass
class CompressedImage(IdlStruct, typename='sensor_msgs/CompressedImage'):
    header: Header = Header() # Header timestamp should be acquisition time of image
                              # Header frame_id should be optical frame of camera
                              # origin of frame should be optical center of cameara
                              # +x should point to the right in the image
                              # +y should point down in the image
                              # +z should point into to plane of the image

    format: str = '' # Specifies the format of the data
                     #   Acceptable values:
                     #     jpeg, png, tiff

    data: sequence[uint8] = default_field([]) # Compressed image buffer
