#/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    n = len(vals)
    if n == 0:
        raise ValueError("values must contain at least one element")

    mean = sum(vals) / n
    squared_diffs = [(x - mean) ** 2 for x in vals]
    return math.sqrt(sum(squared_diffs) / n)

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))
    
    print(stdDev(vals))
