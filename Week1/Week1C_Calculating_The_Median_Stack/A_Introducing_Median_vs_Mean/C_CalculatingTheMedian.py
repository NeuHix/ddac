def whatMedianWithoutStatistics(list):
	if len(list) > 0:
		list.sort()
		# If the len of list is odd -> only one middle value
		if len(list) % 2 != 0:
			middleValue = list[len(list)//2]
			return middleValue
		# If the len of list is even -> TW0 middle values
		else:
			mid = len(list) // 2
			median = (list[mid - 1] + list[mid]) / 2
			return median


if __name__ == '__main__':
	print(whatMedianWithoutStatistics([17.3, 70.1, 22.3, 16.2]))
