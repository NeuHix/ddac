import numpy as np
from ..A_Labelling_The_Sky.E_ConvertToDecimalDegrees import hms2dec


def import_bss():
	reqArray = np.loadtxt('bss.dat', usecols=range(1, 7))
	hms2dec()

	return reqArray

def import_super():
	reqArray = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=[0, 1])

	return reqArray


