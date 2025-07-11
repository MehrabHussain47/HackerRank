#/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#

def weightedMean(V, W):
    # Write your code here
    weighted_sum = 0
    for i in range(len(vals)):
        weighted_sum += vals[i] * weights[i]
    total_weight = sum(weights)

    weighted_mean = weighted_sum / total_weight
    
    print(f"{weighted_mean:.1f}")

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)
