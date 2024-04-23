# foxglove_msgs/msg/ImageAnnotations
# Array of annotations for a 2D image

# Generated by https://github.com/foxglove/schemas

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import sequence
from .CircleAnnotation import CircleAnnotation
from .PointsAnnotation import PointsAnnotation
from .TextAnnotation import TextAnnotation
from .. import default_field

@dataclass
class ImageAnnotations(IdlStruct, typename='foxglove_msgs/ImageAnnotations'):
    # Circle annotations
    circles: sequence[CircleAnnotation] = default_field([])

    # Points annotations
    points: sequence[PointsAnnotation] = default_field([])

    # Text annotations
    texts: sequence[TextAnnotation] = default_field([])