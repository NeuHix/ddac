from astropy.io import fits
import numpy as np


def load_fits(file):
	hduList = fits.open(file)
	imageDataArray = hduList[0].data
	largestValue = np.amax(imageDataArray)
	arrayIndices = np.where(imageDataArray == largestValue)
	indexTuples = (arrayIndices[0][0], arrayIndices[1][0])
	return indexTuples


if __name__ == '__main__':
	print(load_fits('image2.fits'))
