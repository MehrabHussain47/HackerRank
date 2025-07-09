#/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    S = []
    for i in range(len(values)):
        S.extend([values[i]] * freqs[i])
    
    S.sort()

    def median(arr):
        n = len(arr)
        mid = n // 2
        if n % 2 == 0:
            return (arr[mid - 1] + arr[mid]) / 2
        else:
            return arr[mid]

    n = len(S)
    if n % 2 == 0:
        lower_half = S[:n // 2]
        upper_half = S[n // 2:]
    else:
        lower_half = S[:n // 2]
        upper_half = S[n // 2 + 1:]

    Q1 = median(lower_half)
    Q3 = median(upper_half)

    IQR = round(Q3 - Q1, 1)
    print(IQR)

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
