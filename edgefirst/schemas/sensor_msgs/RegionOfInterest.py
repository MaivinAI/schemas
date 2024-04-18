# This message is used to specify a region of interest within an image.
#
# When used to specify the ROI setting of the camera when the image was
# taken, the height and width fields should either match the height and
# width fields for the associated image; or height = width = 0
# indicates that the full resolution image was captured.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import uint32

@dataclass
class RegionOfInterest(IdlStruct, typename='sensor_msgs/RegionOfInterest'):
    x_offset: uint32 = 0  # Leftmost pixel of the ROI
                          # (0 if the ROI includes the left edge of the image)
    y_offset: uint32 = 0  # Topmost pixel of the ROI
                          # (0 if the ROI includes the top edge of the image)
    height: uint32 = 0    # Height of ROI
    width: uint32 = 0     # Width of ROI

    # True if a distinct rectified ROI should be calculated from the "raw"
    # ROI in this message. Typically this should be False if the full image
    # is captured (ROI not used), and True if a subwindow is captured (ROI
    # used).
    do_rectify: bool = False