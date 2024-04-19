# This represents a vector in free space.

# This is semantically different than a point.
# A vector is always anchored at the origin.
# When a transform is applied to a vector, only the rotational component is applied.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float64

@dataclass
class Vector3(IdlStruct, typename='geometry_msgs/Vector3'):
    x: float64 = 0
    y: float64 = 0
    z: float64 = 0