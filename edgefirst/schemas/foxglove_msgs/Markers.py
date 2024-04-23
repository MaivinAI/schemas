# foxglove_msgs/msg/Markers
# A list of any number or type of markers

# Generated by https://github.com/foxglove/schemas

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import sequence
from .MarkerDeletion import MarkerDeletion
from .ArrowMarker import ArrowMarker
from .CubeListMarker import CubeListMarker
from .SphereListMarker import SphereListMarker
from .ConeListMarker import ConeListMarker
from .LineMarker import LineMarker
from .TriangleListMarker import TriangleListMarker
from .TextMarker import TextMarker
from .ModelMarker import ModelMarker
from .. import default_field

@dataclass
class Markers(IdlStruct, typename='foxglove_msgs/Markers'):
    # Marker deletion actions
    deletions: sequence[MarkerDeletion] = default_field([])

    # Arrow markers
    arrows: sequence[ArrowMarker] = default_field([])

    # Cube list markers
    cubes: sequence[CubeListMarker] = default_field([])

    # Sphere list markers
    spheres: sequence[SphereListMarker] = default_field([])

    # Cone list markers
    cones: sequence[ConeListMarker] = default_field([])

    # Line markers
    lines: sequence[LineMarker] = default_field([])

    # Triangle list markers
    triangles: sequence[TriangleListMarker] = default_field([])

    # Text markers
    texts: sequence[TextMarker] = default_field([])

    # Model markers
    models: sequence[ModelMarker] = default_field([])