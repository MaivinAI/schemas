# This is a message to hold data from an IMU (Inertial Measurement Unit)
#
# Accelerations should be in m/s^2 (not in g's), and rotational velocity should be in rad/sec
#
# If the covariance of the measurement is known, it should be filled in (if all you know is the
# variance of each measurement, e.g. from the datasheet, just put those along the diagonal)
# A covariance matrix of all zeros will be interpreted as "covariance unknown", and to use the
# data a covariance will have to be assumed or gotten from some other source
#
# If you have no estimate for one of the data elements (e.g. your IMU doesn't produce an
# orientation estimate), please set element 0 of the associated covariance matrix to -1
# If you are interpreting this message, please check for a value of -1 in the first element of each
# covariance matrix, and disregard the associated estimate.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float64, array
from ..std_msgs.Header import Header
from ..geometry_msgs.Quaternion import Quaternion
from ..geometry_msgs.Vector3 import Vector3
from .. import default_field

@dataclass
class Imu(IdlStruct, typename='sensor_msgs/Imu'):
    header: Header = Header()

    orientation: Quaternion = Quaternion()
    orientation_covariance: array[float64, 9] = default_field([0] * 9) # Row major about x, y, z axes

    angular_velocity: Vector3 = Vector3()
    angular_velocity_covariance: array[float64, 9] = default_field([0] * 9) # Row major about x, y, z axes

    linear_acceleration: Vector3 = Vector3()
    linear_acceleration_covariance: array[float64, 9] = default_field([0] * 9) # Row major x, y z