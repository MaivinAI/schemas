# Radar Information Message Interface - edgefirst/msg/RadarInfo
#
# This interface carries Radar Information related to the device configuration.

std_msgs/Header header

# Radar center frequency band.
#
# Values: low, medium, high
#
string center_frequency

# The frequency sweep controls the detection range of the radar.  The following
# breakdown gives a general range at which a vehicle-type object should be detected.
#
# ultra-short:  9m (requires CENTER_FREQUENCY="low")
# short:       19m
# medium:      56m
# long:       130m
#
string frequency_sweep

# The range-toggle mode allows the radar to alternate between various frequency
# sweep configurations.  Applications must handle range toggling as targets will
# not be consistent between messages as the frequency alternates.
#
# Values: off, short-medium, short-long, medium-long, long-ultra-short, medium-ultra-short, short-ultra-short
#
string range_toggle

# The detection sensitivity only affects the radar target list (point-cloud) and
# controls the sensitivity to recognize a target.  The default is medium, the
# low and high sensitivity options will result in less and more targets, respectively.
#
# Values: low, medium, high
#
string detection_sensitivity

# Radar Data Cube streaming flag, true when enabled.
#
bool cube