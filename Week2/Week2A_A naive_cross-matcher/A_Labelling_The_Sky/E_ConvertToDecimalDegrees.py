def hms2dec(hrs, mins, secs):
	result = 15 * (hrs + mins / 60 + secs / (60 * 60))
	return result


def dms2dec(degs, arcmin, arcsec):
	positiveAngle = 1
	if degs < 0:
		positiveAngle = -1
	result = positiveAngle * (abs(degs) + arcmin / 60 + arcsec / (60 * 60))
	return result


if __name__ == '__main__':
	print(hms2dec(23, 12, 6))
	print(dms2dec(22, 57, 18))

	print(dms2dec(-66, 5, 5.1))
