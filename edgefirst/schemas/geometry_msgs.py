from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float32, float64, array, sequence
from . import default_field
from .std_msgs import Header

@dataclass
class Quaternion(IdlStruct, typename='geometry_msgs/Quaternion'):
    """
    This represents an orientation in free space in quaternion form.
    """
    x: float64 = 0
    y: float64 = 0
    z: float64 = 0
    w: float64 = 1

@dataclass
class QuaternionStamped(IdlStruct, typename='geometry_msgs/QuaternionStamped'):
    """
    This represents an orientation with reference coordinate frame and timestamp.
    """
    header: Header = default_field(Header)
    quaternion: Quaternion = default_field(Quaternion)

@dataclass
class Vector3(IdlStruct, typename='geometry_msgs/Vector3'):
    """
    This represents a vector in free space.
    This is semantically different than a point.
    A vector is always anchored at the origin.
    When a transform is applied to a vector, only the rotational component is applied.
    """
    x: float64 = 0
    y: float64 = 0
    z: float64 = 0

@dataclass
class Vector3Stamped(IdlStruct, typename='geometry_msgs/Vector3Stamped'):
    """
    This represents a Vector3 with reference coordinate frame and timestamp
    Note that this follows vector semantics with it always anchored at the origin,
    so the rotational elements of a transform are the only parts applied when transforming.
    """
    header: Header = default_field(Header)
    vector: Vector3 = default_field(Vector3)

@dataclass
class Accel(IdlStruct, typename='geometry_msgs/Accel'):
    """
    This expresses acceleration in free space broken into its linear and angular parts.
    """
    linear: Vector3 = default_field(Vector3)
    angular: Vector3 = default_field(Vector3)

@dataclass
class AccelStamped(IdlStruct, typename='geometry_msgs/AccelStamped'):
    """
    An accel with reference coordinate frame and timestamp
    """
    header: Header = default_field(Header)
    accel: Accel = default_field(Accel)

@dataclass
class AccelWithCovariance(IdlStruct, typename='geometry_msgs/AccelWithCovariance'):
    """
    This expresses acceleration in free space with uncertainty.
    """
    accel: Accel = default_field(Accel)
    
    covariance: array[float64, 36] = default_field([0] * 36)
    """
    Row-major representation of the 6x6 covariance matrix
    The orientation parameters use a fixed-axis representation.
    In order, the parameters are:
    (x, y, z, rotation about X axis, rotation about Y axis, rotation about Z axis)
    """

@dataclass
class AccelWithCovarianceStamped(IdlStruct, typename='geometry_msgs/AccelWithCovarianceStamped'):
    """
    This represents an estimated accel with reference coordinate frame and timestamp.
    """
    header: Header = default_field(Header)
    accel: AccelWithCovariance = default_field(AccelWithCovariance)

@dataclass
class Inertia(IdlStruct, typename='geometry_msgs/Inertia'):
    m: float64 = 0
    """
    Mass [kg]
    """

    com: Vector3 = default_field(Vector3)
    """
    Center of mass [m]
    """

    ixx: float64 = 0
    ixy: float64 = 0
    ixz: float64 = 0
    iyy: float64 = 0
    iyz: float64 = 0
    izz: float64 = 0
    """
    Inertia Tensor [kg-m^2]
        | ixx ixy ixz |
    I = | ixy iyy iyz |
        | ixz iyz izz |
    """

@dataclass
class InertiaStamped(IdlStruct, typename='geometry_msgs/InertiaStamped'):
    """
    An Inertia with a time stamp and reference frame.
    """
    header: Header = default_field(Header)
    inertia: Inertia = default_field(Inertia)

@dataclass
class Point(IdlStruct, typename='geometry_msgs/Point'):
    """
    This contains the position of a point in free space
    """
    x: float64 = 0
    y: float64 = 0
    z: float64 = 0

@dataclass
class Point32(IdlStruct, typename='geometry_msgs/Point32'):
    """
    This contains the position of a point in free space(with 32 bits of precision).
    It is recommended to use Point wherever possible instead of Point32.
    This recommendation is to promote interoperability.
    This message is designed to take up less space when sending
    lots of points at once, as in the case of a PointCloud.
    """
    x: float32 = 0
    y: float32 = 0
    z: float32 = 0

@dataclass
class PointStamped(IdlStruct, typename='geometry_msgs/PointStamped'):
    """
    This represents a Point with reference coordinate frame and timestamp
    """
    header: Header = default_field(Header)
    point: Point = default_field(Point)

@dataclass
class Polygon(IdlStruct, typename='geometry_msgs/Polygon'):
    """
    A specification of a polygon where the first and last points are assumed to be connected
    """
    points: sequence[Point32] = default_field([])

@dataclass
class PolygonStamped(IdlStruct, typename='geometry_msgs/PolygonStamped'):
    """
    This represents a Polygon with reference coordinate frame and timestamp
    """
    header: Header = default_field(Header)
    polygon: Polygon = default_field(Polygon)

@dataclass
class Pose(IdlStruct, typename='geometry_msgs/Pose'):
    """
    A representation of pose in free space, composed of position and orientation.
    """
    position: Point = default_field(Point)
    orientation: Quaternion = default_field(Quaternion)

@dataclass
class Pose2D(IdlStruct, typename='geometry_msgs/Pose2D'):
    """
    Deprecated as of Foxy and will potentially be removed in any following release.
    Please use the full 3D pose.

    In general our recommendation is to use a full 3D representation of everything and 
    for 2D specific applications make the appropriate projections into the plane for 
    their calculations but optimally will preserve the 3D information during processing.

    If we have parallel copies of 2D datatypes every UI and other pipeline will end up 
    needing to have dual interfaces to plot everything. And you will end up with 
    not being able to use 3D tools for 2D use cases even if they're completely 
    valid, as you'd have to reimplement it with different inputs and outputs. 
    It's not particularly hard to plot the 2D pose or compute the yaw error for 
    the Pose message and there are already tools and libraries that can do this for you.
    This expresses a position and orientation on a 2D manifold.
    """
    x: float64 = 0
    y: float64 = 0
    theta: float64 = 0

@dataclass
class PoseArray(IdlStruct, typename='geometry_msgs/PoseArray'):
    """
    An array of poses with a header for global reference.
    """
    header: Header = default_field(Header)

    poses: sequence[Pose] = default_field([])

@dataclass
class PoseStamped(IdlStruct, typename='geometry_msgs/PoseStamped'):
    """
    A Pose with reference coordinate frame and timestamp
    """
    header: Header = default_field(Header)
    pose: Pose = default_field(Pose)

@dataclass
class PoseWithCovariance(IdlStruct, typename='geometry_msgs/PoseWithCovariance'):
    """
    This represents a pose in free space with uncertainty.
    """
    pose: Pose = default_field(Pose)

    covariance: array[float64, 36] = default_field([0] * 36)
    """
    Row-major representation of the 6x6 covariance matrix
    The orientation parameters use a fixed-axis representation.
    In order, the parameters are:
    (x, y, z, rotation about X axis, rotation about Y axis, rotation about Z axis)
    """

@dataclass
class PoseWithCovarianceStamped(IdlStruct, typename='geometry_msgs/PoseWithCovarianceStamped'):
    """
    This expresses an estimated pose with a reference coordinate frame and timestamp
    """
    header: Header = default_field(Header)
    pose: PoseWithCovariance = default_field(PoseWithCovariance)

@dataclass
class Transform(IdlStruct, typename='geometry_msgs/Transform'):
    """
    This represents the transform between two coordinate frames in free space.
    """
    translation: Vector3 = default_field(Vector3)
    rotation: Quaternion = default_field(Quaternion)

@dataclass
class TransformStamped(IdlStruct, typename='geometry_msgs/TransformStamped'):
    """
    This expresses a transform from coordinate frame header.frame_id
    to the coordinate frame child_frame_id at the time of header.stamp

    This message is mostly used by the
    <a href="https://index.ros.org/p/tf2/">tf2</a> package.
    See its documentation for more information.

    The child_frame_id is necessary in addition to the frame_id
    in the Header to communicate the full reference for the transform
    in a self contained message.
    """

    header: Header = default_field(Header)
    """
    The frame id in the header is used as the reference frame of this transform.
    """

    child_frame_id: str = ''
    """
    The frame id of the child frame to which this transform points.
    """

    transform: Transform = default_field(Transform)
    """
    Translation and rotation in 3-dimensions of child_frame_id from header.frame_id.
    """

@dataclass
class Twist(IdlStruct, typename='geometry_msgs/Twist'):
    """
    This expresses velocity in free space broken into its linear and angular parts.
    """
    linear: Vector3 = default_field(Vector3)
    angular: Vector3 = default_field(Vector3)

@dataclass
class TwistStamped(IdlStruct, typename='geometry_msgs/TwistStamped'):
    """
    A twist with reference coordinate frame and timestamp
    """
    header: Header = default_field(Header)
    twist: Twist = default_field(Twist)

@dataclass
class TwistWithCovariance(IdlStruct, typename='geometry_msgs/TwistWithCovariance'):
    """
    This expresses velocity in free space with uncertainty.
    """
    twist: Twist = default_field(Twist)

    covariance: array[float64, 36] = default_field([0] * 36)
    """
    Row-major representation of the 6x6 covariance matrix
    The orientation parameters use a fixed-axis representation.
    In order, the parameters are:
    (x, y, z, rotation about X axis, rotation about Y axis, rotation about Z axis)
    """

@dataclass
class TwistWithCovarianceStamped(IdlStruct, typename='geometry_msgs/TwistWithCovarianceStamped'):
    """
    This represents an estimated twist with reference coordinate frame and timestamp.
    """
    header: Header = default_field(Header)
    twist: TwistWithCovariance = default_field(TwistWithCovariance)

@dataclass
class Wrench(IdlStruct, typename='geometry_msgs/Wrench'):
    """
    This represents force in free space, separated into its linear and angular parts.
    """
    force: Vector3 = default_field(Vector3)
    torque: Vector3 = default_field(Vector3)

@dataclass
class WrenchStamped(IdlStruct, typename='geometry_msgs/WrenchStamped'):
    """
    A wrench with reference coordinate frame and timestamp
    """
    header: Header = default_field(Header)
    wrench: Wrench = default_field(Wrench)