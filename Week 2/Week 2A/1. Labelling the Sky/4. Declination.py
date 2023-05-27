"""
Declination, on the other hand, is traditionally recorded in degrees-minutes-seconds (DMS) notation.
A full circle is 360 degrees, each degree has 60 arcminutes and each arcminute has 60 arcseconds.

For example: 73 degrees, 21 arcminutes and 14.4 arcseconds (written 73:21:14.4 or 73° 21' 14.4" or 73d21m14.4s)
can be converted to decimal degrees like this:
"""

DecToDeg = 73 + 21/60 + 14.4/(60*60)

'''
With negative angles like -5° 31' 12" the negation applies to the whole angle,
including arcminutes and arcseconds:
'''

negDecToDeg = -1 * (5 + 31/60 + 12/(60*60))
