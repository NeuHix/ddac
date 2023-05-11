import numpy as np

# Without Np
def calc_stats(CSVfile):
	makingListOfLists = []
	finalResult = []
	index = 0

	for lines in open(CSVfile):
		makingListOfLists.append(lines.strip().split(','))

	LengthOfList = len(makingListOfLists)

	for makingFloat in range(0, LengthOfList):
		for elements in makingListOfLists[index]:
			floats = float(elements)
			finalResult.append(floats)
		index += 1

	MeanOfCSV = np.mean(finalResult)
	roundedMean = np.round(MeanOfCSV, decimals=1)
	MedianOfCSV = np.median(finalResult)
	roundedMedian = np.round(MedianOfCSV, decimals=1)
	tuples = (roundedMean, roundedMedian)

	return tuples

# With Np
def calc_statsNP(file):
	NpArray = np.loadtxt(file, delimiter=',')

	roundedMean = np.round(np.mean(NpArray), decimals=1)
	roundedMedian = np.round(np.median(NpArray), decimals=1)
	tuples = (roundedMean, roundedMedian)

	return tuples

