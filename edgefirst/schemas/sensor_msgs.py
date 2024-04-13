from dataclasses import dataclass, field
from pycdr2 import IdlStruct
from pycdr2.types import float64, uint32, sequence, array
from .std_msgs import Header
from . import default_field


@dataclass
class RegionOfInterest(IdlStruct, typename='RegionOfInterest'):
    x_offset: uint32 = 0 # Leftmost pixel of the ROI
    y_offset: uint32 = 0 # Topmost pixel of the ROI
    height: uint32 = 0 # Height of ROI
    width: uint32 = 0 # Width of ROI
    do_rectify: bool = False


@dataclass
class CameraInfo(IdlStruct, typename='CameraInfo'):
    header: Header = Header()
    height: uint32 = 0
    width: uint32 = 0
    distortion_model: str = ''
    d: sequence[float64] = default_field([])
    k: array[float64, 9] = default_field([0] * 9) # 3x3 row-major matrix
    r: array[float64, 9] = default_field([0] * 9) # 3x3 row-major matrix
    p: array[float64, 12] = default_field([0] * 12) # 3x4 row-major matrix
    binning_x: uint32 = 0
    binning_y: uint32 = 0
    roi: RegionOfInterest = RegionOfInterest()
