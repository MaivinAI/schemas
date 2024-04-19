# Single scan from a planar laser range-finder
#
# If you have another ranging device with different behavior (e.g. a sonar
# array), please find or create a different message, since applications
# will make fairly laser-specific assumptions about this data

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float32, sequence
from ..std_msgs.Header import Header
from .. import default_field

@dataclass
class LaserScan(IdlStruct, typename='sensor_msgs/LaserScan'):
    header: Header = Header() # timestamp in the header is the acquisition time of
                              # the first ray in the scan.
                              #
                              # in frame frame_id, angles are measured around
                              # the positive Z axis (counterclockwise, if Z is up)
                              # with zero angle being forward along the x axis

    angle_min: float32 = 0 # start angle of the scan [rad]
    angle_max: float32 = 0 # end angle of the scan [rad]
    angle_increment: float32 = 0 # angular distance between measurements [rad]

    time_increment: float32 = 0 # time between measurements [seconds] - if your scanner
                                # is moving, this will be used in interpolating position
                                # of 3d points
    scan_time: float32 = 0 # time between scans [seconds]

    range_min: float32 = 0 # minimum range value [m]
    range_max: float32 = 0 # maximum range value [m]

    ranges: sequence[float32] = default_field([]) # range data [m]
                                                  # (Note: values < range_min or > range_max should be discarded)
    intensities: sequence[float32] = default_field([]) # intensity data [device-specific units].  If your
                                                       # device does not provide intensities, please leave
                                                       # the array empty.