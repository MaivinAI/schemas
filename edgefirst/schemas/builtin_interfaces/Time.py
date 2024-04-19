# This message communicates ROS Time defined here:
# https://design.ros2.org/articles/clock_and_time.html

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import int32, uint32

@dataclass
class Time(IdlStruct, typename='builtin_interfaces/Time'):
    # The seconds component, valid over all int32 values.
    sec: int32 = 0
    # The nanoseconds component, valid in the range [0, 10e9).
    nanosec: uint32 = 0