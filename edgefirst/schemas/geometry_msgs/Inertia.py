from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float64
from .Vector3 import Vector3

@dataclass
class Inertia(IdlStruct, typename='geometry_msgs/Inertia'):
    # Mass [kg]
    m: float64 = 0

    # Center of mass [m]
    com: Vector3 = Vector3()

    # Inertia Tensor [kg-m^2]
    #     | ixx ixy ixz |
    # I = | ixy iyy iyz |
    #     | ixz iyz izz |
    ixx: float64 = 0
    ixy: float64 = 0
    ixz: float64 = 0
    iyy: float64 = 0
    iyz: float64 = 0
    izz: float64 = 0