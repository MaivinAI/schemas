# This message contains an uncompressed image
# (0, 0) is at top-left corner of image

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import uint32, uint8, sequence
from ..std_msgs.Header import Header
from .. import default_field

@dataclass
class Image(IdlStruct, typename='sensor_msgs/Image'):
    header: Header = Header() # Header timestamp should be acquisition time of image
                              # Header frame_id should be optical frame of camera
                              # origin of frame should be optical center of cameara
                              # +x should point to the right in the image
                              # +y should point down in the image
                              # +z should point into to plane of the image
                              # If the frame_id here and the frame_id of the CameraInfo
                              # message associated with the image conflict
                              # the behavior is undefined

    height: uint32 = 0 # image height, that is, number of rows
    width: uint32 = 0 # image width, that is, number of columns

    # The legal values for encoding are in file src/image_encodings.cpp
    # If you want to standardize a new string format, join
    # ros-users@lists.ros.org and send an email proposing a new encoding.

    encoding: str = '' # Encoding of pixels -- channel meaning, ordering, size
                       # taken from the list of strings in include/sensor_msgs/image_encodings.hpp

    is_bigendian: uint8 = 0 # is this data bigendian?
    step: uint32 = 0 # Full row length in bytes
    data: sequence[uint8] = default_field([]) # actual matrix data, size is (step * rows)