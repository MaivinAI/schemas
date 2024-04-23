# foxglove_msgs/msg/FrameTransformList
# A list of transforms between reference frames in 3D space

# Generated by https://github.com/foxglove/schemas

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import sequence
from .FrameTransform import FrameTransform
from .. import default_field

@dataclass
class FrameTransformList(IdlStruct, typename='foxglove_msgs/FrameTransformList'):
    # List of transforms
    transforms: sequence[FrameTransform] = default_field([])