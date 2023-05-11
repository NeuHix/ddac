import numpy as np


def mean_datasets(filesAsInput):
	currentListIndex = 0
	indexInsideList = 0

	ArrayFiles = []
	RowList = []
	calc_meanList = []
	meanList = []
	threeCalcMeans = []

	for fileToArray in filesAsInput:
		filesMadeArray = np.loadtxt(fileToArray, delimiter=',')
		ArrayFiles.append(filesMadeArray)

	print(ArrayFiles)

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
		resultMean = np.round(np.mean(CalcMean), decimals=1)
		threeCalcMeans.append(resultMean)
		if len(threeCalcMeans) == dimensionOfArrayWeGot[1]:
			meanList.append(threeCalcMeans)
			threeCalcMeans = []

	ArrayedMeans = np.array(meanList)

	return ArrayedMeans


if __name__ == '__main__':
	test = mean_datasets(['data1.csv', 'data2.csv', 'data3.csv'])
	print(test.shape)
