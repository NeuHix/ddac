import numpy as np
from astropy.io import fits


def mean_fits(filesAsInput):
	currentListIndex = 0
	indexInsideList = 0

	ArrayFiles = []
	RowList = []
	calc_meanList = []
	meanList = []
	threeCalcMeans = []

	for fileToArray in filesAsInput:
		hduLists = fits.open(fileToArray)
		imageDataArrays = hduLists[0].data
		ArrayFiles.append(imageDataArrays)

	dimensionOfArrayWeGot = np.shape(ArrayFiles[0])

	for RowLength in range(0, dimensionOfArrayWeGot[0]):
		for columnLength in range(0, dimensionOfArrayWeGot[1]):
			for IterateArray in ArrayFiles:
				RowList.append(IterateArray[currentListIndex][indexInsideList])
			calc_meanList.append(RowList)
			RowList = []
			if indexInsideList < dimensionOfArrayWeGot[1] - 1:
				indexInsideList += 1
		if currentListIndex < dimensionOfArrayWeGot[0]:
			currentListIndex += 1
			indexInsideList = 0

	for CalcMean in calc_meanList:

		threeCalcMeans.append(CalcMean)
		if len(threeCalcMeans) == dimensionOfArrayWeGot[1]:
			meanList.append(threeCalcMeans)
			threeCalcMeans = []

	ArrayedMeans = np.array(meanList)

	return ArrayedMeans


if __name__ == '__main__':
	print(mean_fits(['image0.fits', 'image1.fits', 'image2.fits'])[100, 100])

