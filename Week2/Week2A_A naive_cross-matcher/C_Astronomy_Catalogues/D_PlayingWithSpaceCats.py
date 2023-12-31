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


if __name__ == "__main__":
    print(import_bss())
    print(import_super())
