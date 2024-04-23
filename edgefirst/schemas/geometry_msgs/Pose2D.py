# Deprecated as of Foxy and will potentially be removed in any following release.
# Please use the full 3D pose.

# In general our recommendation is to use a full 3D representation of everything and for 2D specific applications make the appropriate projections into the plane for their calculations but optimally will preserve the 3D information during processing.

# If we have parallel copies of 2D datatypes every UI and other pipeline will end up needing to have dual interfaces to plot everything. And you will end up with not being able to use 3D tools for 2D use cases even if they're completely valid, as you'd have to reimplement it with different inputs and outputs. It's not particularly hard to plot the 2D pose or compute the yaw error for the Pose message and there are already tools and libraries that can do this for you.# This expresses a position and orientation on a 2D manifold.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float64

@dataclass
class Pose2D(IdlStruct, typename='geometry_msgs/Pose2D'):
    x: float64 = 0
    y: float64 = 0
    theta: float64 = 0