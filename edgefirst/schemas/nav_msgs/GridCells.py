# An array of cells in a 2D grid

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float32, sequence
from ..std_msgs.Header import Header
from ..geometry_msgs.Point import Point
from .. import default_field

@dataclass
class GridCells(IdlStruct, typename='nav_msgs/GridCells'):
    header: Header = Header()

    # Width of each cell
    cell_width: float32 = 0

    # Height of each cell
    cell_height: float32 = 0

    # Each cell is represented by the Point at the center of the cell
    cells: sequence[Point] = default_field([])