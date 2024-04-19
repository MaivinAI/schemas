# Constants are chosen to match the enums in the linux kernel
# defined in include/linux/power_supply.h as of version 3.7
# The one difference is for style reasons the constants are
# all uppercase not mixed case.

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float32, uint8, sequence
from ..std_msgs.Header import Header
from .. import default_field
from enum import Enum

# Power supply status constants
class PowerSupplyStatus(Enum):
    POWER_SUPPLY_STATUS_UNKNOWN = 0
    POWER_SUPPLY_STATUS_CHARGING = 1
    POWER_SUPPLY_STATUS_DISCHARGING = 2
    POWER_SUPPLY_STATUS_NOT_CHARGING = 3
    POWER_SUPPLY_STATUS_FULL = 4

# Power supply health constants
class PowerSupplyHealth(Enum):
    POWER_SUPPLY_HEALTH_UNKNOWN = 0
    POWER_SUPPLY_HEALTH_GOOD = 1
    POWER_SUPPLY_HEALTH_OVERHEAT = 2
    POWER_SUPPLY_HEALTH_DEAD = 3
    POWER_SUPPLY_HEALTH_OVERVOLTAGE = 4
    POWER_SUPPLY_HEALTH_UNSPEC_FAILURE = 5
    POWER_SUPPLY_HEALTH_COLD = 6
    POWER_SUPPLY_HEALTH_WATCHDOG_TIMER_EXPIRE = 7
    POWER_SUPPLY_HEALTH_SAFETY_TIMER_EXPIRE = 8

# Power supply technology (chemistry) constants
class PowerSupplyTech(Enum):
    POWER_SUPPLY_TECHNOLOGY_UNKNOWN = 0
    POWER_SUPPLY_TECHNOLOGY_NIMH = 1
    POWER_SUPPLY_TECHNOLOGY_LION = 2
    POWER_SUPPLY_TECHNOLOGY_LIPO = 3
    POWER_SUPPLY_TECHNOLOGY_LIFE = 4
    POWER_SUPPLY_TECHNOLOGY_NICD = 5
    POWER_SUPPLY_TECHNOLOGY_LIMN = 6

@dataclass
class BatteryState(IdlStruct, typename='sensor_msgs/BatteryState'):
    header: Header = Header()
    voltage: float32 = 0 # Voltage in Volts (Mandatory)
    temperature: float32 = 0 # Temperature in Degrees Celsius (If unmeasured NaN)
    current: float32 = 0 # Negative when discharging (A)  (If unmeasured NaN)
    charge: float32 = 0 # Current charge in Ah  (If unmeasured NaN)
    capacity: float32 = 0 # Capacity in Ah (last full capacity)  (If unmeasured NaN)
    design_capacity: float32 = 0 # Capacity in Ah (design capacity)  (If unmeasured NaN)
    percentage: float32 = 0 # Charge percentage on 0 to 1 range  (If unmeasured NaN)
    power_supply_status: uint8 = 0 # The charging status as reported. Values defined above
    power_supply_health: uint8 = 0 # The battery health metric. Values defined above
    power_supply_technology: uint8 = 0 # The battery chemistry. Values defined above
    present: bool = False # True if the battery is present

    cell_voltage: sequence[float32] = default_field([]) # An array of individual cell voltages for each cell in the pack
                                                        # If individual voltages unknown but number of cells known set each to NaN
    cell_temperature: sequence[float32] = default_field([]) # An array of individual cell temperatures for each cell in the pack
                                                            # If individual temperatures unknown but number of cells known set each to NaN
    location: str = '' # The location into which the battery is inserted. (slot number or plug)
    serial_number: str = '' # The best approximation of the battery serial number
