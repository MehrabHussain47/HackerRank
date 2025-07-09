#/bin/python3

import math
import os
import random
import re
import sys

# Print your answer to 1 decimal place within this function
#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    s = []
    for i in range(len(values)):
        s.extend([values[i]] * freqs[i])
    
    s.sort()
    
    n = len(s)
    
    def find_median(arr):
        length = len(arr)
        if length % 2 == 0:
            mid1_idx = length // 2 - 1
            mid2_idx = length // 2
            median = (arr[mid1_idx] + arr[mid2_idx]) / 2
        else:
            median = float(arr[length // 2])
        return median

    mid_index = n // 2

    if n % 2 == 0:
        lower_half = s[:mid_index]
        upper_half = s[mid_index:]
    else:
        lower_half = s[:mid_index]
        upper_half = s[mid_index + 1:]
        
    q1 = find_median(lower_half)
    q3 = find_median(upper_half)

    interquartile_range = q3 - q1
    print(f"{interquartile_range:.1f}")

if __name__ == '__main__':
    try:
        n = int(input().strip())
        val = list(map(int, input().rstrip().split()))
        freq = list(map(int, input().rstrip().split()))
        
        interQuartile(val, freq)
    except (EOFError, RuntimeError):
        print("Running with example data as input is not available.")
        print("Example: values = [6, 12, 8, 10, 20, 16], freqs = [5, 4, 3, 2, 1, 5]")

