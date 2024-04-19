# Duration defines a period between two time points.

# Messages of this datatype are of ROS Time following this design:

# https://design.ros2.org/articles/clock_and_time.html

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import int32, uint32

@dataclass
class Duration(IdlStruct, typename='builtin_interfaces/Duration'):
    # The seconds component, valid over all int32 values.
    sec: int32 = 0
    # The nanoseconds component, valid in the range [0, 10e9).
    nanosec: uint32 = 0