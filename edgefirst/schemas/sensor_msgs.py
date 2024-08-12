from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float32, float64, int8, int32, uint8, uint16, uint32, array, sequence
from . import default_field
from .std_msgs import Header
from .builtin_interfaces import Time
from .geometry_msgs import Point32, Quaternion, Transform, Twist, Wrench, Vector3
from enum import Enum

class PowerSupplyStatus(Enum):
    """
    Power supply status constants
    """
    POWER_SUPPLY_STATUS_UNKNOWN = 0
    POWER_SUPPLY_STATUS_CHARGING = 1
    POWER_SUPPLY_STATUS_DISCHARGING = 2
    POWER_SUPPLY_STATUS_NOT_CHARGING = 3
    POWER_SUPPLY_STATUS_FULL = 4

class PowerSupplyHealth(Enum):
    """
    Power supply health constants
    """
    POWER_SUPPLY_HEALTH_UNKNOWN = 0
    POWER_SUPPLY_HEALTH_GOOD = 1
    POWER_SUPPLY_HEALTH_OVERHEAT = 2
    POWER_SUPPLY_HEALTH_DEAD = 3
    POWER_SUPPLY_HEALTH_OVERVOLTAGE = 4
    POWER_SUPPLY_HEALTH_UNSPEC_FAILURE = 5
    POWER_SUPPLY_HEALTH_COLD = 6
    POWER_SUPPLY_HEALTH_WATCHDOG_TIMER_EXPIRE = 7
    POWER_SUPPLY_HEALTH_SAFETY_TIMER_EXPIRE = 8

class PowerSupplyTech(Enum):
    """
    Power supply technology (chemistry) constants
    """
    POWER_SUPPLY_TECHNOLOGY_UNKNOWN = 0
    POWER_SUPPLY_TECHNOLOGY_NIMH = 1
    POWER_SUPPLY_TECHNOLOGY_LION = 2
    POWER_SUPPLY_TECHNOLOGY_LIPO = 3
    POWER_SUPPLY_TECHNOLOGY_LIFE = 4
    POWER_SUPPLY_TECHNOLOGY_NICD = 5
    POWER_SUPPLY_TECHNOLOGY_LIMN = 6

@dataclass
class RegionOfInterest(IdlStruct, typename='sensor_msgs/RegionOfInterest'):
    """
    This message is used to specify a region of interest within an image.
    
    When used to specify the ROI setting of the camera when the image was
    taken, the height and width fields should either match the height and
    width fields for the associated image; or height = width = 0
    indicates that the full resolution image was captured.
    """
    x_offset: uint32 = 0 
    """
    Leftmost pixel of the ROI
    (0 if the ROI includes the left edge of the image)
    """
    y_offset: uint32 = 0
    """
    Topmost pixel of the ROI
    (0 if the ROI includes the top edge of the image)
    """
    height: uint32 = 0
    """
    Height of ROI
    """
    width: uint32 = 0 
    """
    Width of ROI
    """

    do_rectify: bool = False
    """
    True if a distinct rectified ROI should be calculated from the "raw"
    ROI in this message. Typically this should be False if the full image
    is captured (ROI not used), and True if a subwindow is captured (ROI
    used).
    """

@dataclass
class BatteryState(IdlStruct, typename='sensor_msgs/BatteryState'):
    """
    Constants are chosen to match the enums in the linux kernel
    defined in include/linux/power_supply.h as of version 3.7
    The one difference is for style reasons the constants are
    all uppercase not mixed case.
    """
    header: Header = default_field(Header)
    voltage: float32 = 0 
    """
    Voltage in Volts (Mandatory)
    """
    temperature: float32 = 0
    """
    Temperature in Degrees Celsius (If unmeasured NaN)
    """
    current: float32 = 0
    """
    Negative when discharging (A)  (If unmeasured NaN)
    """
    charge: float32 = 0
    """
    Current charge in Ah  (If unmeasured NaN)
    """
    capacity: float32 = 0
    """
    Capacity in Ah (last full capacity)  (If unmeasured NaN)
    """
    design_capacity: float32 = 0
    """
    Capacity in Ah (design capacity)  (If unmeasured NaN)
    """
    percentage: float32 = 0
    """
    Charge percentage on 0 to 1 range  (If unmeasured NaN)
    """
    power_supply_status: uint8 = 0
    """
    The charging status as reported. Values defined above
    """
    power_supply_health: uint8 = 0
    """
    The battery health metric. Values defined above
    """
    power_supply_technology: uint8 = 0
    """
    The battery chemistry. Values defined above
    """
    present: bool = False
    """
    True if the battery is present
    """
    cell_voltage: sequence[float32] = default_field([]) 
    """
    An array of individual cell voltages for each cell in the pack
    If individual voltages unknown but number of cells known set each to NaN
    """
    cell_temperature: sequence[float32] = default_field([]) 
    """
    An array of individual cell temperatures for each cell in the pack
    If individual temperatures unknown but number of cells known set each to NaN
    """
    location: str = ''
    """
    The location into which the battery is inserted. (slot number or plug)
    """
    serial_number: str = ''
    """
    The best approximation of the battery serial number
    """

@dataclass
class CameraInfo(IdlStruct, typename='sensor_msgs/CameraInfo'):
    """
    This message defines meta information for a camera. It should be in a
    camera namespace on topic "camera_info" and accompanied by up to five
    image topics named:
    
      image_raw - raw data from the camera driver, possibly Bayer encoded
      image            - monochrome, distorted
      image_color      - color, distorted
      image_rect       - monochrome, rectified
      image_rect_color - color, rectified
    
    The image_pipeline contains packages (image_proc, stereo_image_proc)
    for producing the four processed image topics from image_raw and
    camera_info. The meaning of the camera parameters are described in
    detail at http://www.ros.org/wiki/image_pipeline/CameraInfo.
    
    The image_geometry package provides a user-friendly interface to
    common operations using this meta information. If you want to, e.g.,
    project a 3d point into image coordinates, we strongly recommend
    using image_geometry.
    
    If the camera is uncalibrated, the matrices D, K, R, P should be left
    zeroed out. In particular, clients may assume that K[0] == 0.0
    indicates an uncalibrated camera.
    """
    #######################################################################
    #                     Image acquisition info                          #
    #######################################################################
    header: Header = default_field(Header) 
    """
    Time of image acquisition, camera coordinate frame ID
    Header timestamp should be acquisition time of image
    Header frame_id should be optical frame of camera
    origin of frame should be optical center of camera
    +x should point to the right in the image
    +y should point down in the image
    +z should point into the plane of the image
    """

    #######################################################################
    #                      Calibration Parameters                         #
    #######################################################################
    # These are fixed during camera calibration. Their values will be the #
    # same in all messages until the camera is recalibrated. Note that    #
    # self-calibrating systems may "recalibrate" frequently.              #
    #                                                                     #
    # The internal parameters can be used to warp a raw (distorted) image #
    # to:                                                                 #
    #   1. An undistorted image (requires D and K)                        #
    #   2. A rectified image (requires D, K, R)                           #
    # The projection matrix P projects 3D points into the rectified image.#
    #######################################################################

    # The image dimensions with which the camera was calibrated.
    # Normally this will be the full camera resolution in pixels.
    height: uint32 = 0
    width: uint32 = 0

    distortion_model: str = ''
    """
    The distortion model used. Supported models are listed in
    sensor_msgs/distortion_models.hpp. For most cameras, "plumb_bob" - a
    simple model of radial and tangential distortion - is sufficent.
    """

    d: sequence[float64] = default_field([])
    """
    The distortion parameters, size depending on the distortion model.
    For "plumb_bob", the 5 parameters are: (k1, k2, t1, t2, k3).
    """

    k: array[float64, 9] = default_field([0] * 9)
    """
    3x3 row-major matrix
    Intrinsic camera matrix for the raw (distorted) images.
        [fx  0 cx]
    K = [ 0 fy cy]
        [ 0  0  1]
    Projects 3D points in the camera coordinate frame to 2D pixel
    coordinates using the focal lengths (fx, fy) and principal point
    (cx, cy).
    """

    r: array[float64, 9] = default_field([0] * 9)
    """
    3x3 row-major matrix
    Rectification matrix (stereo cameras only)
    A rotation matrix aligning the camera coordinate system to the ideal
    stereo image plane so that epipolar lines in both stereo images are
    parallel.
    """
    
    p: array[float64, 12] = default_field([0] * 12)
    """
    3x4 row-major matrix
    Projection/camera matrix
        [fx'  0  cx' Tx]
    P = [ 0  fy' cy' Ty]
        [ 0   0   1   0]
    By convention, this matrix specifies the intrinsic (camera) matrix
     of the processed (rectified) image. That is, the left 3x3 portion
     is the normal camera intrinsic matrix for the rectified image.
    It projects 3D points in the camera coordinate frame to 2D pixel
     coordinates using the focal lengths (fx', fy') and principal point
     (cx', cy') - these may differ from the values in K.
    For monocular cameras, Tx = Ty = 0. Normally, monocular cameras will
     also have R = the identity and P[1:3,1:3] = K.
    For a stereo pair, the fourth column [Tx Ty 0]' is related to the
     position of the optical center of the second camera in the first
     camera's frame. We assume Tz = 0 so both cameras are in the same
     stereo image plane. The first camera always has Tx = Ty = 0. For
     the right (second) camera of a horizontal stereo pair, Ty = 0 and
     Tx = -fx' * B, where B is the baseline between the cameras.
    Given a 3D point [X Y Z]', the projection (x, y) of the point onto
     the rectified image is given by:
     [u v w]' = P * [X Y Z 1]'
            x = u / w
            y = v / w
     This holds for both images of a stereo pair.
    """
    #######################################################################
    #                      Operational Parameters                         #
    #######################################################################
    # These define the image region actually captured by the camera       #
    # driver. Although they affect the geometry of the output image, they #
    # may be changed freely without recalibrating the camera.             #
    #######################################################################

    # Binning refers here to any camera setting which combines rectangular
    #  neighborhoods of pixels into larger "super-pixels." It reduces the
    #  resolution of the output image to
    #  (width / binning_x) x (height / binning_y).
    # The default values binning_x = binning_y = 0 is considered the same
    #  as binning_x = binning_y = 1 (no subsampling).
    binning_x: uint32 = 0
    binning_y: uint32 = 0

    roi: RegionOfInterest = default_field(RegionOfInterest)
    """
    Region of interest (subwindow of full camera resolution), given in
     full resolution (unbinned) image coordinates. A particular ROI
     always denotes the same window of pixels on the camera sensor,
     regardless of binning settings.
    The default setting of roi (all values 0) is considered the same as
     full resolution (roi.width = width, roi.height = height).
    """

@dataclass
class ChannelFloat32(IdlStruct, typename='sensor_msgs/ChannelFloat32'):
    """
    This message is used by the PointCloud message to hold optional data
    associated with each point in the cloud. The length of the values
    array should be the same as the length of the points array in the
    PointCloud, and each value should be associated with the corresponding
    point.
    
    Channel names in existing practice include:
      "u", "v" - row and column (respectively) in the left stereo image.
                 This is opposite to usual conventions but remains for
                 historical reasons. The newer PointCloud2 message has no
                 such problem.
      "rgb" - For point clouds produced by color stereo cameras. uint8
              (R,G,B) values packed into the least significant 24 bits,
              in order.
      "intensity" - laser or pixel intensity.
      "distance"
    """
    
    name: str = ''
    """
    The channel name should give semantics of the channel (e.g.
    "intensity" instead of "value").
    """

    values: sequence[float32] = default_field([])
    """
    The values array should be 1-1 with the elements of the associated
    PointCloud.
    """

@dataclass
class CompressedImage(IdlStruct, typename='sensor_msgs/CompressedImage'):
    """
    This message contains a compressed image.
    """
    header: Header = default_field(Header) 
    """
    Header timestamp should be acquisition time of image
    Header frame_id should be optical frame of camera
    origin of frame should be optical center of cameara
    +x should point to the right in the image
    +y should point down in the image
    +z should point into to plane of the image
    """
    format: str = '' 
    """
    Specifies the format of the data
      Acceptable values:
        jpeg, png, tiff
    """
    data: sequence[uint8] = default_field([])
    """
    Compressed image buffer
    """

@dataclass
class FluidPressure(IdlStruct, typename='sensor_msgs/FluidPressure'):
    """
    Single pressure reading.  This message is appropriate for measuring the
    pressure inside of a fluid (air, water, etc).  This also includes
    atmospheric or barometric pressure.
    
    This message is not appropriate for force/pressure contact sensors.
    """
    header: Header = default_field(Header)
    """
    timestamp of the measurement
    frame_id is the location of the pressure sensor
    """
    fluid_pressure: float64 = 0
    """
    Absolute pressure reading in Pascals.
    """
    variance: float64 = 0
    """
    0 is interpreted as variance unknown
    """

@dataclass
class Illuminance(IdlStruct, typename='sensor_msgs/Illuminance'):
    """
    Single photometric illuminance measurement.  Light should be assumed to be
    measured along the sensor's x-axis (the area of detection is the y-z plane).
    The illuminance should have a 0 or positive value and be received with
    the sensor's +X axis pointing toward the light source.
    
    Photometric illuminance is the measure of the human eye's sensitivity of the
    intensity of light encountering or passing through a surface.
    
    All other Photometric and Radiometric measurements should not use this message.
    This message cannot represent:
     - Luminous intensity (candela/light source output)
     - Luminance (nits/light output per area)
     - Irradiance (watt/area), etc.
    """
    header: Header = default_field(Header)
    """
    timestamp is the time the illuminance was measured
    frame_id is the location and direction of the reading
    """
    illuminance: float64 = 0
    """
    Measurement of the Photometric Illuminance in Lux.
    """
    variance: float64 = 0 
    """
    0 is interpreted as variance unknown
    """

@dataclass
class Image(IdlStruct, typename='sensor_msgs/Image'):
    """
    This message contains an uncompressed image
    (0, 0) is at top-left corner of image
    """
    header: Header = default_field(Header) 
    """
    Header timestamp should be acquisition time of image
    Header frame_id should be optical frame of camera
    origin of frame should be optical center of cameara
    +x should point to the right in the image
    +y should point down in the image
    +z should point into to plane of the image
    If the frame_id here and the frame_id of the CameraInfo
    message associated with the image conflict
    the behavior is undefined
    """
    height: uint32 = 0
    """
    image height, that is, number of rows
    """
    width: uint32 = 0
    """
    image width, that is, number of columns
    """
    
    encoding: str = ''
    """
    The legal values for encoding are in file src/image_encodings.cpp
    If you want to standardize a new string format, join
    ros-users@lists.ros.org and send an email proposing a new encoding.
    Encoding of pixels -- channel meaning, ordering, size
    taken from the list of strings in include/sensor_msgs/image_encodings.hpp
    """
    is_bigendian: uint8 = 0
    """
    is this data bigendian?
    """
    step: uint32 = 0
    """
    Full row length in bytes
    """
    data: sequence[uint8] = default_field([])
    """
    actual matrix data, size is (step * rows)
    """

@dataclass
class Imu(IdlStruct, typename='sensor_msgs/Imu'):
    """
    This is a message to hold data from an IMU (Inertial Measurement Unit)
    
    Accelerations should be in m/s^2 (not in g's), and rotational velocity should be in rad/sec
    
    If the covariance of the measurement is known, it should be filled in (if all you know is the
    variance of each measurement, e.g. from the datasheet, just put those along the diagonal)
    A covariance matrix of all zeros will be interpreted as "covariance unknown", and to use the
    data a covariance will have to be assumed or gotten from some other source
    
    If you have no estimate for one of the data elements (e.g. your IMU doesn't produce an
    orientation estimate), please set element 0 of the associated covariance matrix to -1
    If you are interpreting this message, please check for a value of -1 in the first element of each
    covariance matrix, and disregard the associated estimate.
    """
    header: Header = default_field(Header)

    orientation: Quaternion = default_field(Quaternion)
    orientation_covariance: array[float64, 9] = default_field([0] * 9)
    """
    Row major about x, y, z axes
    """

    angular_velocity: Vector3 = default_field(Vector3)
    angular_velocity_covariance: array[float64, 9] = default_field([0] * 9)
    """
    Row major about x, y, z axes
    """

    linear_acceleration: Vector3 = default_field(Vector3)
    linear_acceleration_covariance: array[float64, 9] = default_field([0] * 9)
    """
    Row major x, y z
    """

@dataclass
class JointState(IdlStruct, typename='sensor_msgs/JointState'):
    """
    This is a message that holds data to describe the state of a set of torque controlled joints.
    
    The state of each joint (revolute or prismatic) is defined by:
     * the position of the joint (rad or m),
     * the velocity of the joint (rad/s or m/s) and
     * the effort that is applied in the joint (Nm or N).
    
    Each joint is uniquely identified by its name
    The header specifies the time at which the joint states were recorded. All the joint states
    in one message have to be recorded at the same time.
    
    This message consists of a multiple arrays, one for each part of the joint state.
    The goal is to make each of the fields optional. When e.g. your joints have no
    effort associated with them, you can leave the effort array empty.
    
    All arrays in this message should have the same size, or be empty.
    This is the only way to uniquely associate the joint name with the correct
    states.
    """
    header: Header = default_field(Header)

    name: sequence[str] = default_field([])
    position: sequence[float64] = default_field([])
    velocity: sequence[float64] = default_field([])
    effort: sequence[float64] = default_field([])

@dataclass
class Joy(IdlStruct, typename='sensor_msgs/Joy'):
    """
    Reports the state of a joystick's axes and buttons.
    """
    header: Header = default_field(Header)
    """
    The timestamp is the time at which data is received from the joystick.
    """

    axes: sequence[float32] = default_field([])
    """
    The axes measurements from a joystick.
    """

    buttons: sequence[int32] = default_field([])
    """
    The buttons measurements from a joystick.
    """

class FeedbackType(Enum):
    TYPE_LED    = 0
    TYPE_RUMBLE = 1
    TYPE_BUZZER = 2

@dataclass
class JoyFeedback(IdlStruct, typename='sensor_msgs/JoyFeedback'):
    type: uint8 = 0
    """
    Declare of the type of feedback
    """

    id: uint8 = 0
    """
    This will hold an id number for each type of each feedback.
    Example, the first led would be id=0, the second would be id=1
    """

    intensity: float32 = 0
    """
    Intensity of the feedback, from 0.0 to 1.0, inclusive.  If device is
    actually binary, driver should treat 0<=x<0.5 as off, 0.5<=x<=1 as on.
    """

@dataclass
class JoyFeedbackArray(IdlStruct, typename='sensor_msgs/JoyFeedbackArray'):
    """
    This message publishes values for multiple feedback at once.
    """
    array: sequence[JoyFeedback] = default_field([])

@dataclass
class LaserEcho(IdlStruct, typename='sensor_msgs/LaserEcho'):
    """
    This message is a submessage of MultiEchoLaserScan and is not intended
    to be used separately.
    """
    echoes: sequence[float32] = default_field([])  
    """
    Multiple values of ranges or intensities.
    Each array represents data from the same angle increment.
    """

@dataclass
class LaserScan(IdlStruct, typename='sensor_msgs/LaserScan'):
    """
    Single scan from a planar laser range-finder
    
    If you have another ranging device with different behavior (e.g. a sonar
    array), please find or create a different message, since applications
    will make fairly laser-specific assumptions about this data
    """
    header: Header = default_field(Header) 
    """
    timestamp in the header is the acquisition time of
    the first ray in the scan.
    
    in frame frame_id, angles are measured around
    the positive Z axis (counterclockwise, if Z is up)
    with zero angle being forward along the x axis
    """
    angle_min: float32 = 0
    """
    start angle of the scan [rad]
    """
    angle_max: float32 = 0
    """
    end angle of the scan [rad]
    """
    angle_increment: float32 = 0
    """
    angular distance between measurements [rad]
    """
    time_increment: float32 = 0 
    """
    time between measurements [seconds] - if your scanner
    is moving, this will be used in interpolating position
    of 3d points
    """
    scan_time: float32 = 0
    """
    time between scans [seconds]
    """
    range_min: float32 = 0
    """
    minimum range value [m]
    """
    range_max: float32 = 0
    """
    maximum range value [m]
    """
    ranges: sequence[float32] = default_field([])
    """ 
    range data [m]
    (Note: values < range_min or > range_max should be discarded)
    """
    intensities: sequence[float32] = default_field([])
    """
    intensity data [device-specific units].  If your
    device does not provide intensities, please leave
    the array empty.
    """

@dataclass
class MagneticField(IdlStruct, typename='sensor_msgs/MagneticField'):
    """
    Measurement of the Magnetic Field vector at a specific location.
    
    If the covariance of the measurement is known, it should be filled in.
    If all you know is the variance of each measurement, e.g. from the datasheet,
    just put those along the diagonal.
    A covariance matrix of all zeros will be interpreted as "covariance unknown",
    and to use the data a covariance will have to be assumed or gotten from some
    other source.
    """
    header: Header = default_field(Header) 
    """
    timestamp is the time the
    field was measured
    frame_id is the location and orientation
    of the field measurement
    """
    magnetic_field: Vector3 = default_field(Vector3)
    """
    x, y, and z components of the
    field vector in Tesla
    If your sensor does not output 3 axes,
    put NaNs in the components not reported.
    """
    magnetic_field_covariance: array[float64, 9] = default_field([0] * 9)
    """
    Row major about x, y, z axes
    0 is interpreted as variance unknown
    """

@dataclass
class MultiDOFJointState(IdlStruct, typename='sensor_msgs/MultiDOFJointState'):
    """
    Representation of state for joints with multiple degrees of freedom,
    following the structure of JointState which can only represent a single degree of freedom.
    
    It is assumed that a joint in a system corresponds to a transform that gets applied
    along the kinematic chain. For example, a planar joint (as in URDF) is 3DOF (x, y, yaw)
    and those 3DOF can be expressed as a transformation matrix, and that transformation
    matrix can be converted back to (x, y, yaw)
    
    Each joint is uniquely identified by its name
    The header specifies the time at which the joint states were recorded. All the joint states
    in one message have to be recorded at the same time.
    
    This message consists of a multiple arrays, one for each part of the joint state.
    The goal is to make each of the fields optional. When e.g. your joints have no
    wrench associated with them, you can leave the wrench array empty.
    
    All arrays in this message should have the same size, or be empty.
    This is the only way to uniquely associate the joint name with the correct
    states.
    """
    header: Header = default_field(Header)

    joint_names: sequence[str] = default_field([])
    transforms: sequence[Transform] = default_field([])
    twist: sequence[Twist] = default_field([])
    wrench: sequence[Wrench] = default_field([])

@dataclass
class MultiEchoLaserScan(IdlStruct, typename='sensor_msgs/MultiEchoLaserScan'):
    """
    Single scan from a multi-echo planar laser range-finder
    
    If you have another ranging device with different behavior (e.g. a sonar
    array), please find or create a different message, since applications
    will make fairly laser-specific assumptions about this data
    """
    header: Header = default_field(Header) 
    """
    timestamp in the header is the acquisition time of
    the first ray in the scan.
    
    in frame frame_id, angles are measured around
    the positive Z axis (counterclockwise, if Z is up)
    with zero angle being forward along the x axis
    """
    angle_min: float32 = 0
    """
    start angle of the scan [rad]
    """
    angle_max: float32 = 0
    """
    end angle of the scan [rad]
    """
    angle_increment: float32 = 0
    """
    angular distance between measurements [rad]
    """
    time_increment: float32 = 0
    """
    time between measurements [seconds] - if your scanner
    is moving, this will be used in interpolating position
    of 3d points
    """
    scan_time: float32 = 0
    """
    time between scans [seconds]
    """
    range_min: float32 = 0
    """
    minimum range value [m]
    """
    range_max: float32 = 0
    """
    maximum range value [m]
    """
    ranges: sequence[LaserEcho] = default_field([])
    """
    range data [m]
    (Note: NaNs, values < range_min or > range_max should be discarded)
    +Inf measurements are out of range
    -Inf measurements are too close to determine exact distance.
    """
    intensities: sequence[LaserEcho] = default_field([])
    """
    intensity data [device-specific units].  If your
    device does not provide intensities, please leave
    the array empty.
    """

class GpsStatus(Enum):
    STATUS_NO_FIX =  -1        # unable to fix position
    STATUS_FIX =      0        # unaugmented fix
    STATUS_SBAS_FIX = 1        # with satellite-based augmentation
    STATUS_GBAS_FIX = 2        # with ground-based augmentation

class GpsService(Enum):
    SERVICE_GPS =     1
    SERVICE_GLONASS = 2
    SERVICE_COMPASS = 4      # includes BeiDou.
    SERVICE_GALILEO = 8

@dataclass
class NavSatStatus(IdlStruct, typename='sensor_msgs/NavSatStatus'):
    """
    Navigation Satellite fix status for any Global Navigation Satellite System.
    
    Whether to output an augmented fix is determined by both the fix
    type and the last time differential corrections were received.  A
    fix is valid when status >= STATUS_FIX.
    """
    status: int8 = 0
    """
    Bits defining which Global Navigation Satellite System signals were
    used by the receiver.
    """
    service: uint16 = 0

class CovarianceType(Enum):
    COVARIANCE_TYPE_UNKNOWN = 0
    COVARIANCE_TYPE_APPROXIMATED = 1
    COVARIANCE_TYPE_DIAGONAL_KNOWN = 2
    COVARIANCE_TYPE_KNOWN = 3

@dataclass
class NavSatFix(IdlStruct, typename='sensor_msgs/NavSatFix'):
    """
    Navigation Satellite fix for any Global Navigation Satellite System
    
    Specified using the WGS 84 reference ellipsoid
    """
    
    header: Header = default_field(Header)
    """
    header.stamp specifies the ROS time for this measurement (the
           corresponding satellite time may be reported using the
           sensor_msgs/TimeReference message).
    
    header.frame_id is the frame of reference reported by the satellite
           receiver, usually the location of the antenna.  This is a
           Euclidean frame relative to the vehicle, not a reference
           ellipsoid.
    """

    status: NavSatStatus = default_field(NavSatStatus)
    """
    Satellite fix status information.
    """

    latitude: float64 = 0
    """
    Latitude [degrees]. Positive is north of equator; negative is south.
    """

    longitude: float64 = 0
    """
    Longitude [degrees]. Positive is east of prime meridian; negative is west.
    """

    altitude: float64 = 0
    """
    Altitude [m]. Positive is above the WGS 84 ellipsoid
    (quiet NaN if no altitude is available).
    """

    position_covariance: array[float64, 9] = default_field([0] * 9)
    """
    Position covariance [m^2] defined relative to a tangential plane
    through the reported position. The components are East, North, and
    Up (ENU), in row-major order.
    
    Beware: this coordinate system exhibits singularities at the poles.
    """

    position_covariance_type: uint8 = 0
    """
    If the covariance of the fix is known, fill it in completely. If the
    GPS receiver provides the variance of each measurement, put them
    along the diagonal. If only Dilution of Precision is available,
    estimate an approximate covariance from that.
    """

@dataclass
class PointCloud(IdlStruct, typename='sensor_msgs/PointCloud'):
    """
    # THIS MESSAGE IS DEPRECATED AS OF FOXY
    # Please use sensor_msgs/PointCloud2

    This message holds a collection of 3d points, plus optional additional
    information about each point.
    """
    header: Header = default_field(Header)
    """
    Time of sensor data acquisition, coordinate frame ID.
    """

    points: sequence[Point32] = default_field([])
    """
    Array of 3d points. Each Point32 should be interpreted as a 3d point
    in the frame given in the header.
    """

    channels: sequence[ChannelFloat32] = default_field([])
    """
    Each channel should have the same number of elements as points array,
    and the data in each channel should correspond 1:1 with each point.
    Channel names in common practice are listed in ChannelFloat32.msg.
    """

class PointFieldDatatype(Enum):
    INT8    = 1
    UINT8   = 2
    INT16   = 3
    UINT16  = 4
    INT32   = 5
    UINT32  = 6
    FLOAT32 = 7
    FLOAT64 = 8

@dataclass
class PointField(IdlStruct, typename='sensor_msgs/PointField'):
    """
    This message holds the description of one point entry in the
    PointCloud2 message format.
    """
    name: str = ''
    """
    Name of field
    Common PointField names are x, y, z, intensity, rgb, rgba
    """
    offset: uint32 = 0
    """
    Offset from start of point struct
    """
    datatype: uint8 = 0
    """
    Datatype enumeration, see above
    """
    count: uint32 = 0
    """
    How many elements in the field
    """

@dataclass
class PointCloud2(IdlStruct, typename='sensor_msgs/PointCloud2'):
    """
    This message holds a collection of N-dimensional points, which may
    contain additional information such as normals, intensity, etc. The
    point data is stored as a binary blob, its layout described by the
    contents of the "fields" array.
    
    The point cloud data may be organized 2d (image-like) or 1d (unordered).
    Point clouds organized as 2d images may be produced by camera depth sensors
    such as stereo or time-of-flight.
    """

    header: Header = default_field(Header)
    """
    Time of sensor data acquisition, and the coordinate frame ID (for 3d points).
    """

    # 2D structure of the point cloud. If the cloud is unordered, height is
    # 1 and width is the length of the point cloud.
    height: uint32 = 0
    width: uint32 = 0

    fields: sequence[PointField] = default_field([])
    """
    Describes the channels and their layout in the binary data blob.
    """

    is_bigendian: bool = False 
    """
    Is this data bigendian?
    """
    point_step: uint32 = 0
    """
    Length of a point in bytes
    """
    row_step: uint32 = 0
    """
    Length of a row in bytes
    """
    data: sequence[uint8] = default_field([])
    """
    Actual point data, size is (row_step*height)
    """
    is_dense: bool = False
    """
    True if there are no invalid points
    """

class RadiationType(Enum):
    """
    Radiation type enums
    If you want a value added to this list, send an email to the ros-users list
    """
    ULTRASOUND=0
    INFRARED=1

@dataclass
class Range(IdlStruct, typename='sensor_msgs/Range'):
    """
    Single range reading from an active ranger that emits energy and reports
    one range reading that is valid along an arc at the distance measured.
    This message is  not appropriate for laser scanners. See the LaserScan
    message if you are working with a laser scanner.
    
    This message also can represent a fixed-distance (binary) ranger.  This
    sensor will have min_range===max_range===distance of detection.
    These sensors follow REP 117 and will output -Inf if the object is detected
    and +Inf if the object is outside of the detection range.
    """
    header: Header = default_field(Header)
    """
    timestamp in the header is the time the ranger
    returned the distance reading
    """

    radiation_type: uint8 = 0
    """
    the type of radiation used by the sensor
    (sound, IR, etc) [enum]
    """
    field_of_view: float32 = 0
    """
    the size of the arc that the distance reading is
    valid for [rad]
    the object causing the range reading may have
    been anywhere within -field_of_view/2 and
    field_of_view/2 at the measured range.
    0 angle corresponds to the x-axis of the sensor.
    """

    min_range: float32 = 0
    """
    minimum range value [m]
    """
    max_range: float32 = 0
    """
    maximum range value [m]
    Fixed distance rangers require min_range==max_range
    """
    range: float32 = 0
    """ 
    range data [m]
    (Note: values < range_min or > range_max should be discarded)
    Fixed distance rangers only output -Inf or +Inf.
    -Inf represents a detection within fixed distance.
    (Detection too close to the sensor to quantify)
    +Inf represents no detection within the fixed distance.
    (Object out of range)
    """

@dataclass
class RelativeHumidity(IdlStruct, typename='sensor_msgs/RelativeHumidity'):
    """
    Single reading from a relative humidity sensor.
    Defines the ratio of partial pressure of water vapor to the saturated vapor
    pressure at a temperature.
    """
    header: Header = default_field(Header)
    """
    timestamp of the measurement
    frame_id is the location of the humidity sensor
    """
    relative_humidity: float64 = 0 
    """
    Expression of the relative humidity
    from 0.0 to 1.0.
    0.0 is no partial pressure of water vapor
    1.0 represents partial pressure of saturation
    """
    variance: float64 = 0
    """
    0 is interpreted as variance unknown
    """

@dataclass
class Temperature(IdlStruct, typename='sensor_msgs/Temperature'):
    """
    Single temperature reading.
    """
    header: Header = default_field(Header) 
    """
    timestamp is the time the temperature was measured
    frame_id is the location of the temperature reading
    """
    temperature: float64 = 0
    """
    Measurement of the Temperature in Degrees Celsius.
    """
    variance: float64 = 0
    """
    0 is interpreted as variance unknown.
    """

@dataclass
class TimeReference(IdlStruct, typename='sensor_msgs/TimeReference'):
    """
    Measurement from an external time source not actively synchronized with the system clock.
    """
    header: Header = default_field(Header) 
    """
    stamp is system time for which measurement was valid
    frame_id is not used
    """
    time_ref: Time = default_field(Time)
    """
    corresponding time from this external source
    """
    source: str = ''
    """
    (optional) name of time source
    """
