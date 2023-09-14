import numpy as np


def hms2dec(hrs, mins, secs):
    result = 15 * (hrs + mins / 60 + secs / (60 * 60))
    return result


def dms2dec(degs, arcmin, arcsec):
    positiveAngle = 1
    if degs < 0:
        positiveAngle = -1
    result = positiveAngle * (abs(degs) + arcmin / 60 + arcsec / (60 * 60))
    return result


def import_bss():
    bssList = []
    npbss = np.loadtxt("bss.dat", usecols=range(1, 7))

    for id, row in enumerate(npbss, 1):
        bssList.append(
            (id, hms2dec(row[0], row[1], row[2]), dms2dec(row[3], row[4], row[5]))
        )
    return bssList


def import_super():
    supList = []
    npsup = np.loadtxt("super.csv", delimiter=",", skiprows=1, usecols=(0, 1))

    for id, row in enumerate(npsup, 1):
        supList.append((id, row[0], row[1]))
    return supList


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


def find_closest(catalog, ra, dec):
    min_dist = np.inf
    reqID = 0

    for id, ra1, dec1 in catalog:
        dist = angular_dist(ra1, dec1, ra, dec)
        if min_dist > dist:
            min_dist = dist
            reqID = id

    return reqID, min_dist


if __name__ == "__main__":
    cat = import_bss()
    print(find_closest(cat, 32.2, 40.7))
