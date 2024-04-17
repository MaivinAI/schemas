from dataclasses import dataclass, field
import copy
from pycdr2 import IdlStruct
from pycdr2.types import uint32, float64, int32, array, sequence

def default_field(obj):
    return field(default_factory=lambda: copy.copy(obj))

@dataclass
class RegionOfInterest(IdlStruct, typename='RegionOfInterest'):
    x_offset: uint32 = 0 # Leftmost pixel of the ROI
    y_offset: uint32 = 0 # Topmost pixel of the ROI
    height: uint32 = 0 # Height of ROI
    width: uint32 = 0 # Width of ROI
    do_rectify: bool = False

@dataclass
class Time(IdlStruct, typename='Time'):
    sec: int32 = 0
    nanosec: uint32 = 0

@dataclass
class Header(IdlStruct, typename='Header'):
    stamp: Time = Time()
    frame_id: str = ''

@dataclass
class CameraInfo(IdlStruct, typename='CameraInfo'):
    header: Header = Header() # Header timestamp should be acquisition time of image
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

