# This message holds the description of one point entry in the
# PointCloud2 message format.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import uint32, uint8
from enum import Enum

class Datatype(Enum):
    INT8    = 1
    UINT8   = 2
    INT16   = 3
    UINT16  = 4
    INT32   = 5
    UINT32  = 6
    FLOAT32 = 7
    FLOAT64 = 8

@dataclass
class PointField(IdlStruct, typename='sensor_msgs/PointField'):
    # Common PointField names are x, y, z, intensity, rgb, rgba
    name: str = '' # Name of field
    offset: uint32 = 0 # Offset from start of point struct
    datatype: uint8 = 0 # Datatype enumeration, see above
    count: uint32 = 0 # How many elements in the field