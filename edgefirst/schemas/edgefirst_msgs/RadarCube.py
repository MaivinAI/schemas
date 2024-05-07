# Radar Cube Message Interface - edgefirst/msg/RadarCube
#
# The RadarCube interface carries various radar cube reprensentations of the
# Radar FFT before generally being processed by CFAR into a point cloud.  The
# cube coud be R, RD, RAD, RA, and so on where R=Range, D=Dopper, and A=Azimuth.

# Dimensional labels are used to describe the radar cube layout.  Not all cubes
# include every label.  Undefined is used for dimensions not covered by this list.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import sequence, uint8, uint16, uint64, int16, float32
from ..std_msgs import Header
from .. import default_field
from enum import Enum

class RadarMode(Enum):
    UNDEFINED = 0
    RANGE = 1
    DOPPLER = 2
    AZIMUTH = 3
    ELEVATION = 4
    RXCHANNEL = 5
    SEQUENCE = 6


@dataclass
class RadarCube(IdlStruct, typename='edgefirst_msgs/RadarCube'):
    header: Header = Header()
    timestamp: uint64 = 0 # Radar frame timestamp generated on the radar module
    layout: sequence[uint8] = default_field([]) # Radar cube layout provides labels for each dimensions
    shape: sequence[uint16] = default_field([]) # Radar cube shape provides the shape of each dimensions
    scales: sequence[float32] = default_field([]) # The scaling factors for the dimensions representing bins
                                                  # For dimensions taken "as-is" the scale will be 1.0
    cube: sequence[int16] = default_field([]) # The radar cube data as 16bit integers.  If the is_complex
                                              # is true then each element will be pairs of integers with
                                              # the first being real and the second being imaginary
    is_complex: bool = False # True if the radar cube is complex in which case the final
                             # dimension will be doubled in size to account for the pair
                             # of int16 elements representing [real,imaginary].