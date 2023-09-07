import time
import statistics
import numpy as np

def time_stat(func, sizeofArray, times):
	randArray = np.random.randn(sizeofArray)
	avgList = []

	for instance in range(times):
		timeStart = time.perf_counter()
		data = func(randArray)
		timeOver = time.perf_counter()
		timlapse = timeOver - timeStart
		avgList.append(timlapse)

	return sum(avgList) / times

if __name__ == '__main__':
	print('{:.6f}s for statistics.mean'.format(time_stat(statistics.mean, 10 ** 5, 10)))
	print('{:.6f}s for np.mean'.format(time_stat(np.mean, 10 ** 5, 1000)))