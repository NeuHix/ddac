"""
Right ascension is often given in hours-minutes-seconds (HMS) notation,
because it was convenient to calculate when a star would appear over the horizon.
A full circle in HMS notation is 24 hours, which means 1 hour in HMS notation is equal to 15 degrees.

Each hour is split into 60 minutes and each minute into 60 seconds.

You can convert 23 hours, 12 minutes and 6 seconds (written as 23:12:06 or 23h12m06s) to degrees like this:
"""


def RAtoDegs(hrs, mins, secs):
	result = 15 * (hrs + mins / 60 + secs / (60 * 60))

	return result
