"""
Measuring how much memory python objects occupy
"""
import sys
import numpy

a = 3
b = 'rnwefweergfrger'

print(sys.getsizeof(numpy.random.rand(10**9)))
