import numpy as np


def angular_dist(ra1, d1, ra2, d2):
	ra1 = np.radians(ra1)
	d1 = np.radians(d1)
	ra2 = np.radians(ra2)
	d2 = np.radians(d2)

	a = np.sin((d1 - d2) / 2) ** 2
	b = np.cos(d1) * np.cos(d2) * np.sin(np.abs(ra1 - ra2) / 2) ** 2
	angDis = 2 * np.arcsin(np.sqrt(a + b))
	angDis = np.degrees(angDis)

	return angDis

if __name__ == '__main__':
	print(angular_dist(10.3, -3, 24.3, -29))
