# Navigation Satellite fix for any Global Navigation Satellite System
#
# Specified using the WGS 84 reference ellipsoid

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float64, uint8, array
from ..std_msgs.Header import Header
from .NavSatStatus import NavSatStatus
from .. import default_field
from enum import Enum

class CovarianceType(Enum):
    COVARIANCE_TYPE_UNKNOWN = 0
    COVARIANCE_TYPE_APPROXIMATED = 1
    COVARIANCE_TYPE_DIAGONAL_KNOWN = 2
    COVARIANCE_TYPE_KNOWN = 3

@dataclass
class NavSatFix(IdlStruct, typename='sensor_msgs/NavSatFix'):
    # header.stamp specifies the ROS time for this measurement (the
    #        corresponding satellite time may be reported using the
    #        sensor_msgs/TimeReference message).
    #
    # header.frame_id is the frame of reference reported by the satellite
    #        receiver, usually the location of the antenna.  This is a
    #        Euclidean frame relative to the vehicle, not a reference
    #        ellipsoid.
    header: Header = Header()

    # Satellite fix status information.
    status: NavSatStatus = NavSatStatus()

    # Latitude [degrees]. Positive is north of equator; negative is south.
    latitude: float64 = 0

    # Longitude [degrees]. Positive is east of prime meridian; negative is west.
    longitude: float64 = 0

    # Altitude [m]. Positive is above the WGS 84 ellipsoid
    # (quiet NaN if no altitude is available).
    altitude: float64 = 0

    # Position covariance [m^2] defined relative to a tangential plane
    # through the reported position. The components are East, North, and
    # Up (ENU), in row-major order.
    #
    # Beware: this coordinate system exhibits singularities at the poles.
    position_covariance: array[float64, 9] = default_field([0] * 9)

    # If the covariance of the fix is known, fill it in completely. If the
    # GPS receiver provides the variance of each measurement, put them
    # along the diagonal. If only Dilution of Precision is available,
    # estimate an approximate covariance from that.
    position_covariance_type: uint8 = 0