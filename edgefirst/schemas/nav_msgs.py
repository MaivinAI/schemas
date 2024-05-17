from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float32, int8, uint32, sequence
from . import default_field
from .builtin_interfaces import Time
from .std_msgs import Header
from .geometry_msgs import Point, Pose, PoseStamped, PoseWithCovariance, TwistWithCovariance


@dataclass
class GridCells(IdlStruct, typename='nav_msgs/GridCells'):
    """
    An array of cells in a 2D grid
    """
    header: Header = default_field(Header)

    cell_width: float32 = 0
    """
    Width of each cell
    """

    cell_height: float32 = 0
    """
    Height of each cell
    """

    cells: sequence[Point] = default_field([])
    """
    Each cell is represented by the Point at the center of the cell
    """

@dataclass
class MapMetaData(IdlStruct, typename='nav_msgs/MapMetaData'):
    """
    This hold basic information about the characteristics of the OccupancyGrid
    """
    map_load_time: Time = default_field(Time)
    """
    The time at which the map was loaded
    """

    resolution: float32 = 0
    """
    The map resolution [m/cell]
    """

    width: uint32 = 0
    """
    Map width [cells]
    """

    height: uint32 = 0
    """
    Map height [cells]
    """

    origin: Pose = default_field(Pose)
    """
    The origin of the map [m, m, rad].  This is the real-world pose of the
    bottom left corner of cell (0,0) in the map.
    """

@dataclass
class OccupancyGrid(IdlStruct, typename='nav_msgs/OccupancyGrid'):
    """
    This represents a 2-D grid map
    """
    header: Header = default_field(Header)

    info: MapMetaData = default_field(MapMetaData)
    """
    MetaData for the map
    """

    data: sequence[int8] = default_field([])
    """
    The map data, in row-major order, starting with (0,0). 
    Cell (1, 0) will be listed second, representing the next cell in the x direction. 
    Cell (0, 1) will be at the index equal to info.width, followed by (1, 1).
    The values inside are application dependent, but frequently, 
    0 represents unoccupied, 1 represents definitely occupied, and
    -1 represents unknown. 
    """

@dataclass
class Odometry(IdlStruct, typename='nav_msgs/Odometry'):
    """
    This represents an estimate of a position and velocity in free space.
    The pose in this message should be specified in the coordinate frame given by header.frame_id
    The twist in this message should be specified in the coordinate frame given by the child_frame_id
    """
    header: Header = default_field(Header)
    """
    Includes the frame id of the pose parent.
    """

    child_frame_id: str = ''
    """
    Frame id the pose points to. The twist is in this coordinate frame.
    """

    pose: PoseWithCovariance = default_field(PoseWithCovariance)
    """
    Estimated pose that is typically relative to a fixed world frame.
    """

    twist: TwistWithCovariance = default_field(TwistWithCovariance)
    """
    Estimated linear and angular velocity relative to child_frame_id.
    """

@dataclass
class Path(IdlStruct, typename='nav_msgs/Path'):
    """
    An array of poses that represents a Path for a robot to follow.
    """
    header: Header = default_field(Header)
    """
    Indicates the frame_id of the path.
    """
    poses: sequence[PoseStamped] = default_field([])
    """
    Array of poses to follow.
    """