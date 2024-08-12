from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import sequence, uint8, uint16, uint32, uint64, int16, int32, float32
from . import default_field
from .std_msgs import Header
from .builtin_interfaces import Duration, Time
from enum import Enum


@dataclass
class Date(IdlStruct, typename='edgefirst_msgs/Date'):
    """
    The Date type holds the year, month, and day of the month.  It is used in
    the LocalTime message to represent the date of the local time.
    """
    year: uint16 = 0
    month: uint8 = 0
    day: uint8 = 0


@dataclass
class Date(IdlStruct, typename='edgefirst_msgs/Date'):
    """
    The local time interface publishes the current time on the device.  It is
    mainly intended to allow synchronization of multiple MCAP files by the
    Maivin Publisher.  The idea is to calculate the offset from the timestamp
    in the header with the actual local time, then when multiple MCAP files
    have the local time topic recorded the relative offsets can then be
    calculated.
    """

    header: Header = default_field(Header)
    """Message header containing the timestamp and frame id."""

    date: Date = default_field(Date)
    """
    The base date from which the local time is calculated.  This could be an
    epoch such as the standard UNIX 1 January 1970 or it could be the current
    date.  To calculate the real local time both the date, time, and timezone
    are combined into a valid date and time.
    """

    time: Time = default_field(Time)
    """
    The time offset from the date.  If the date is the current day then the
    time is the normal time of day.  If the date is an epoch than many days
    will be represented in the time.
    """

    timezone: int16 = 0
    """
    The timezone offset in minutes from UTC of the time value.  The timezone
    would be +/- 720 (+/- 12 hours).  Minutes are used to allow for partial
    offsets such as Newfoundland in Canada which is UTC-210 (UTC-3h30).
    """


@dataclass
class Track(IdlStruct, typename='edgefirst_msgs/Track'):
    id: str = ''
    """
    Unique identifier for the object track (if the object is not tracked then "")
    """
    lifetime: int32 = 0
    """
    Number of consecutive frames the object has been tracked
    """
    created: Time = default_field(Time)
    """
    Time the track was first added
    """


@dataclass
class Box(IdlStruct, typename='edgefirst_msgs/Box'):
    center_x: float32 = 0
    """
    Normalized x-coordinate of the center
    """
    center_y: float32 = 0
    """
    Normalized y-coordinate of the center
    """
    width: float32 = 0
    """
    Normalized width of the box
    """
    height: float32 = 0
    """
    Normalized height of the box
    """
    label: str = ''
    """
    object label
    """
    score: float32 = 0
    """
    confidence score for detection
    """
    distance: float32 = 0
    """
    Distance of object (if known)
    """
    speed: float32 = 0
    """
    Speed of object (if known)
    """
    track: Track = default_field(Track)
    """
    object tracking, each track includes ID and lifetime information
    """


@dataclass
class Mask(IdlStruct, typename='edgefirst_msgs/Mask'):
    height: uint32 = 0
    """
    The height of the mask, 0 if this dimension is unused.
    """

    width: uint32 = 0
    """
    The width of the mask, 0 if this dimension is unused.
    """

    length: uint32 = 0
    """
    The length of the mask, 0 if this dimension is unused.  The length would
    be used in 3D masks to represent the depth.  It could also be used for 2D
    bird's eye view masks along with width instead of height (elevation).
    """

    encoding: str = ''
    """
    The optional encoding for the mask (currently unused).
    """

    mask: sequence[uint8] = default_field([])
    """
    The segmentation mask data.  The array should be reshaped according to the
    height, width, and length dimensions.  The dimension order is row-major.
    """


@dataclass
class Model(IdlStruct, typename='edgefirst_msgs/Model'):
    header: Header = Header()
    """
    Metadata including timestamp and coordinate frame
    """

    input_time: Duration = Duration()
    """
    Duration to load inputs into the model
    """

    model_time: Duration = Duration()
    """
    Duration to run the model, not including input/output/decoding
    """

    output_time: Duration = Duration()
    """
    Duration to read outputs from the model
    """

    decode_time: Duration = Duration()
    """
    Duration to decode the outputs from the model, including nms and tracking.
    """

    boxes: sequence[Box] = default_field([])
    """
    Array of detected object bounding boxes.
    """

    mask: sequence[Mask] = default_field([])
    """
    Segmentation masks from the model.  Empty array if model does not generate
    masks.  Generally models will only generate a single mask if they do.
    """


@dataclass
class Detect(IdlStruct, typename='Detect'):
    header: Header = default_field(Header)
    """
    Metadata including timestamp and coordinate frame
    """
    input_timestamp: Time = default_field(Time)
    """
    Timestamp of the input data (e.g., from camera)
    """
    model_time: Time = default_field(Time)
    """
    Timestamp when the object was processed by the model
    """
    output_time: Time = default_field(Time)
    """
    Timestamp when the processed output was available
    """
    boxes: sequence[Box] = default_field([])
    """
    Array of detected object bounding boxes
    """


@dataclass
class DmaBuffer(IdlStruct, typename='DmaBuffer'):
    header: Header = default_field(Header)
    """
    Metadata including timestamp and coordinate frame
    """
    pid: uint32 = 0
    """
    The process id of the service that created the DMA buffer
    """
    fd: int32 = 0
    """
    The file descriptor of the DMA buffer
    """
    width: uint32 = 0
    """
    The width of the image in pixels
    """
    height: uint32 = 0
    """
    The height of the image in pixels
    """
    stride: uint32 = 0
    """
    The stride of the image in bytes
    """
    fourcc: uint32 = 0
    """
    The fourcc code of the image
    """
    length: uint32 = 0
    """
    The length of the DMA buffer in bytes, used to mmap the buffer
    """


class RadarMode(Enum):
    UNDEFINED = 0
    RANGE = 1
    DOPPLER = 2
    AZIMUTH = 3
    ELEVATION = 4
    RXCHANNEL = 5
    SEQUENCE = 6


@dataclass
class RadarCube(IdlStruct, typename='edgefirst_msgs/RadarCube'):
    """
    The RadarCube interface carries various radar cube reprensentations of the
    Radar FFT before generally being processed by CFAR into a point cloud.  The
    cube coud be R, RD, RAD, RA, and so on where R=Range, D=Dopper, and
    A=Azimuth.

    Dimensional labels are used to describe the radar cube layout.  Not all
    cubes include every label.  Undefined is used for dimensions not covered by
    this list.
    """

    header: Header = default_field(Header)
    """Message header containing the timestamp and frame id."""

    timestamp: uint64 = 0
    """Radar frame timestamp generated on the radar module"""

    layout: sequence[uint8] = default_field([])
    """Radar cube layout provides labels for each dimensions"""

    shape: sequence[uint16] = default_field([])
    """Radar cube shape provides the shape of each dimensions"""

    scales: sequence[float32] = default_field([])
    """
    The scaling factors for the dimensions representing bins.  For dimensions
    taken "as-is" the scale will be 1.0.
    """

    cube: sequence[int16] = default_field([])
    """
    The radar cube data as 16bit integers.  If the is_complex is true then each
    element will be pairs of integers with the first being real and the second
    being imaginary.
    """

    is_complex: bool = False
    """
    True if the radar cube is complex in which case the final dimension will be
    doubled in size to account for the pair of int16 elements representing
    [real,imaginary].
    """
