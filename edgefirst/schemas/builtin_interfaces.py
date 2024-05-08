from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import int32, uint32

@dataclass
class Duration(IdlStruct, typename='builtin_interfaces/Duration'):
    """
    Duration defines a period between two time points.
    Messages of this datatype are of ROS Time following this design:
    https://design.ros2.org/articles/clock_and_time.html
    """
    sec: int32 = 0
    """
    The seconds component, valid over all int32 values.
    """
    nanosec: uint32 = 0
    """
    The nanoseconds component, valid in the range [0, 10e9).
    """
    
@dataclass
class Time(IdlStruct, typename='builtin_interfaces/Time'):
    sec: int32 = 0
    """
    The seconds component, valid over all int32 values.
    """
    nanosec: uint32 = 0
    """
    The nanoseconds component, valid in the range [0, 10e9).
    """