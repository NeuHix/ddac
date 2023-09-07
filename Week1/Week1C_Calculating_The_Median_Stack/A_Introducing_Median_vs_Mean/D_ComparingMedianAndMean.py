def list_stats(list):
	list.sort()
	length = len(list)
	if length > 0:
		# mean
		mean = sum(list)/length

		# median
		if length % 2 != 0:
			median = list[length//2]
		else:
			mid = length // 2
			median = (list[mid - 1] + list[mid]) / 2

		MandM = (median, mean)
		return MandM


if __name__ == '__main__':
	print(list_stats([1.3, 2.4, 20.6, 0.95, 3.1]))
