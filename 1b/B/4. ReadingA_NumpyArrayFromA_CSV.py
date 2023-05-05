import numpy as np


# replacement of np's loadtxt function without numpy
def CSVtoList(CSVfile):
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

	return finalResult




print(np.array(CSVtoList("data.csv")))
print(np.loadtxt("B/data.csv", delimiter=','))
