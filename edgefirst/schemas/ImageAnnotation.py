from dataclasses import dataclass, field
import copy
from pycdr2 import IdlStruct
from pycdr2.types import float64, int32, uint32, uint8, sequence

def default_field(obj):
    return field(default_factory=lambda: copy.copy(obj))

@dataclass
class Time(IdlStruct, typename='Time'):
    sec: int32 = 0
    nanosec: uint32 = 0

@dataclass
class Color(IdlStruct, typename='Color'):
    r: float64 = 0
    g: float64 = 0
    b: float64 = 0
    a: float64 = 0

@dataclass
class Point2(IdlStruct, typename='Point2'):
    x: float64 = 0
    y: float64 = 0

@dataclass
class PointsAnnotation(IdlStruct, typename='PointsAnnotation'):
    timestamp: Time = Time()
    UNKNOWN=0
    POINTS=1
    LINE_LOOP=2
    LINE_STRIP=3
    LINE_LIST=4
    type: uint8 = 0
    points: sequence[Point2] = default_field([])
    outline_color: Color = Color()
    outline_colors: sequence[Color] = default_field([])
    fill_color: Color = Color()
    thickness: float64 = 0

@dataclass
class TextAnnotation(IdlStruct, typename='TextAnnotation'):
    timestamp: Time = Time()
    position: Point2 = Point2()
    text: str = ''
    font_size: float64 = 0
    text_color: Color = Color()
    background_color: Color = Color()

@dataclass
class CircleAnnotation(IdlStruct, typename='CircleAnnotation'):
    timestamp: Time = Time()
    position: Point2 = Point2()
    diameter: float64 = 0
    thickness: float64 = 0
    fill_color: Color = Color()
    outline_color: Color = Color()

@dataclass
class ImageAnnotation(IdlStruct, typename='ImageAnnotation'):
    circles: sequence[CircleAnnotation] = default_field([])
    points: sequence[PointsAnnotation] = default_field([])
    texts: sequence[TextAnnotation] = default_field([])

