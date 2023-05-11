makingListOfLists = []


for lines in open('2. NumPy arrays and file IO/data.csv'):
	makingListOfLists.append(lines.strip().split(','))

print(makingListOfLists)