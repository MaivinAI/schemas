# This hold basic information about the characteristics of the OccupancyGrid

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import uint32, float32
from ..builtin_interfaces.Time import Time
from ..geometry_msgs.Pose import Pose

@dataclass
class MapMetaData(IdlStruct, typename='nav_msgs/MapMetaData'):
    # The time at which the map was loaded
    map_load_time: Time = Time()

    # The map resolution [m/cell]
    resolution: float32 = 0

    # Map width [cells]
    width: uint32 = 0

    # Map height [cells]
    height: uint32 = 0

    # The origin of the map [m, m, rad].  This is the real-world pose of the
    # bottom left corner of cell (0,0) in the map.
    origin: Pose = Pose()