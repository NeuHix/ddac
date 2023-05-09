import numpy as np

"""
2D Array Slicing in Numpy
"""

# 1D Array in Numpy
OneDArrayInNp = np.array([1, 3.8, 1.8, 0.8])
print(OneDArrayInNp[::2])

# 2D Array in Numpy
TwoDArrayInNp = np.array([[2, 4.5, 3.6], [3, 4.2, 3.1]])

print(TwoDArrayInNp, "\n")
print(TwoDArrayInNp[0:2, 1])

'''
1D Array Slicing just works like ordinary list slicing 
because, well, it just takes a single list of floats to make one.

2D Array Slicing works little differently.

whole list = [[2, 4.5, 3.6], [3, 4.2, 3.1]]
first daughter list = [2, 4.5, 3.6]
second daughter list = [3, 4.2, 3.1]

It is a list of two lists which contain floats as their elements.
		2dArray[x,y]
		x = which element of the list you want to access ?
			the first element of the "whole list" is the 
			first "daughter list"
		
		y = then you do normal list slicing on the specified 
			"daughter list" in "x"
		
If you wanna do list slicing on both "daughter list" , 
you specify "0:2" or ":" in "x"

learned this here: https://www.w3schools.com/python/numpy/numpy_array_slicing.asp
'''