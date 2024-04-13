from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float64
from .buildin_interfaces import Time


@dataclass
class Header(IdlStruct, typename='Header'):
    """
    Standard metadata for higher-level stamped data types. This is generally
    used to communicate timestamped data in a particular coordinate frame.

    stamp: Time - Timestamp that is expressed as seconds and nanoseconds.
    frame_id: string - Transform frame with which this data is associated.
    """
    stamp: Time = Time()
    frame_id: str = ''


@dataclass
class ColorRGBA(IdlStruct, typename='ColorRGBA'):
    r: float64 = 0.0
    g: float64 = 0.0
    b: float64 = 0.0
    a: float64 = 0.0
