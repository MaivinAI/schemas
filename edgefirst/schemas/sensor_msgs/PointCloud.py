## THIS MESSAGE IS DEPRECATED AS OF FOXY
## Please use sensor_msgs/PointCloud2

# This message holds a collection of 3d points, plus optional additional
# information about each point.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import sequence
from ..std_msgs.Header import Header
from ..geometry_msgs.Point32 import Point32
from .ChannelFloat32 import ChannelFloat32
from .. import default_field

@dataclass
class PointCloud(IdlStruct, typename='sensor_msgs/PointCloud'):
    # Time of sensor data acquisition, coordinate frame ID.
    header: Header = Header()

    # Array of 3d points. Each Point32 should be interpreted as a 3d point
    # in the frame given in the header.
    points: sequence[Point32] = default_field([])

    # Each channel should have the same number of elements as points array,
    # and the data in each channel should correspond 1:1 with each point.
    # Channel names in common practice are listed in ChannelFloat32.msg.
    channels: sequence[ChannelFloat32] = default_field([])