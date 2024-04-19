# This message holds a collection of N-dimensional points, which may
# contain additional information such as normals, intensity, etc. The
# point data is stored as a binary blob, its layout described by the
# contents of the "fields" array.
#
# The point cloud data may be organized 2d (image-like) or 1d (unordered).
# Point clouds organized as 2d images may be produced by camera depth sensors
# such as stereo or time-of-flight.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import uint32, uint8, sequence
from ..std_msgs.Header import Header
from .PointField import PointField
from .. import default_field

@dataclass
class PointCloud2(IdlStruct, typename='sensor_msgs/PointCloud2'):
    # Time of sensor data acquisition, and the coordinate frame ID (for 3d points).
    header: Header = Header()

    # 2D structure of the point cloud. If the cloud is unordered, height is
    # 1 and width is the length of the point cloud.
    height: uint32 = 0
    width: uint32 = 0

    # Describes the channels and their layout in the binary data blob.
    fields: sequence[PointField] = default_field([])

    is_bigendian: bool = False # Is this data bigendian?
    point_step: uint32 = 0 # Length of a point in bytes
    row_step: uint32 = 0 # Length of a row in bytes
    data: sequence[uint8] = default_field([]) # Actual point data, size is (row_step*height)

    is_dense: bool = False # True if there are no invalid points