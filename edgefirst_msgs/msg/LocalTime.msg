# Local Time Message Interface - edgefirst/msg/LocalTime
#
# The local time interface publishes the current time on the device.  It is
# mainly intended to allow synchronization of multiple MCAP files by the Maivin
# Publisher.  The idea is to calculate the offset from the timestamp in the
# header with the actual local time, then when multiple MCAP files have the
# local time topic recorded the relative offsets can then be calculated.

std_msgs/Header header

# The base date from which the local time is calculated.  This could be an
# epoch such as the standard UNIX 1 January 1970 or it could be the current
# date.  To calculate the real local time both the date, time, and timezone are
# combined into a valid date and time.
edgefirst_msgs/Date date

# The time offset from the date.  If the date is the current day then the time
# is the normal time of day.  If the date is an epoch than many days will be
# represented in the time.
builtin_interfaces/Time time

# The timezone offset in minutes from UTC of the time value.  The timezone
# would be +/- 720 (+/- 12 hours).  Minutes are used to allow for partial
# offsets such as Newfoundland in Canada which is UTC-210 (UTC-3h30).
int16 timezone
