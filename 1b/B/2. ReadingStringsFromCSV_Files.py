makingListOfLists = []


for lines in open('B/data.csv'):
	makingListOfLists.append(lines.strip().split(','))

print(makingListOfLists)