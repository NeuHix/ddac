import numpy as np

makingListOfLists = []
finalResult = []
index = 0


for lines in open('2. NumPy arrays and file IO/data.csv'):
	makingListOfLists.append(lines.strip().split(','))

LengthOfList = len(makingListOfLists)

for makingFloat in range(0, LengthOfList):
	for elements in makingListOfLists[index]:
		floats = float(elements)
		finalResult.append(floats)
	index += 1

print(finalResult)

# Np's Asarray Function

print(np.asarray(makingListOfLists, float))
