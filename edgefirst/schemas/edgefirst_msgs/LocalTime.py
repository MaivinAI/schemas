# LocalTime Message Interface - edgefirst_msgs/msg/LocalTime

from dataclasses import dataclass
from . import Date
from ..std_msgs import Header
from ..builtin_interfaces import Time
from pycdr2 import IdlStruct
from pycdr2.types import int16


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

    """
    Message header containing the timestamp and frame id.
    """
    header: Header = Header()

    """
    The base date from which the local time is calculated.  This could be an
    epoch such as the standard UNIX 1 January 1970 or it could be the current
    date.  To calculate the real local time both the date, time, and timezone
    are combined into a valid date and time.
    """
    date: Date = Date()

    """
    The time offset from the date.  If the date is the current day then the
    time is the normal time of day.  If the date is an epoch than many days
    will be represented in the time.
    """
    time: Time = Time()

    """
    The timezone offset in minutes from UTC of the time value.  The timezone
    would be +/- 720 (+/- 12 hours).  Minutes are used to allow for partial
    offsets such as Newfoundland in Canada which is UTC-210 (UTC-3h30).
    """
    timezone: int16 = 0
