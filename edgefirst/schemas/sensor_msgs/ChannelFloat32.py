# This message is used by the PointCloud message to hold optional data
# associated with each point in the cloud. The length of the values
# array should be the same as the length of the points array in the
# PointCloud, and each value should be associated with the corresponding
# point.
#
# Channel names in existing practice include:
#   "u", "v" - row and column (respectively) in the left stereo image.
#              This is opposite to usual conventions but remains for
#              historical reasons. The newer PointCloud2 message has no
#              such problem.
#   "rgb" - For point clouds produced by color stereo cameras. uint8
#           (R,G,B) values packed into the least significant 24 bits,
#           in order.
#   "intensity" - laser or pixel intensity.
#   "distance"

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float32, sequence
from .. import default_field

@dataclass
class ChannelFloat32(IdlStruct, typename='sensor_msgs/ChannelFloat32'):
    # The channel name should give semantics of the channel (e.g.
    # "intensity" instead of "value").
    name: str = ''

    # The values array should be 1-1 with the elements of the associated
    # PointCloud.
    values: sequence[float32] = default_field([])