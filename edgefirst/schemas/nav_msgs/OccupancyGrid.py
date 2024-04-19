# This represents a 2-D grid map

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import int8, sequence
from ..std_msgs.Header import Header
from .MapMetaData import MapMetaData
from .. import default_field

@dataclass
class OccupancyGrid(IdlStruct, typename='nav_msgs/OccupancyGrid'):
    header: Header = Header()

    # MetaData for the map
    info: MapMetaData = MapMetaData()

    # The map data, in row-major order, starting with (0,0). 
    # Cell (1, 0) will be listed second, representing the next cell in the x direction. 
    # Cell (0, 1) will be at the index equal to info.width, followed by (1, 1).
    # The values inside are application dependent, but frequently, 
    # 0 represents unoccupied, 1 represents definitely occupied, and
    # -1 represents unknown. 
    data: sequence[int8] = default_field([])
