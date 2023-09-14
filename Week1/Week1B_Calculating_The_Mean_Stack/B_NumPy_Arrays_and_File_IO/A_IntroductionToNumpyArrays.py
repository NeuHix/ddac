import numpy as np

listOfNumbers = [20, 45, 0.2, 7.8]

NpArrayOfList = np.array(listOfNumbers)

print(NpArrayOfList)
print(f"SizeOfNpArray: {NpArrayOfList.size}")
print(f"MeanOfList: {np.mean(NpArrayOfList)}")
print(f"StandardDeviationOfList: {np.std(listOfNumbers)}")
