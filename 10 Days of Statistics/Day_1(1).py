#/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def median(arr):
    arr.sort()
    n = len(arr)
    mid = n // 2
    if n % 2 == 0:
        return (arr[mid - 1] + arr[mid]) // 2
    else:
        return arr[mid]

def quartiles(arr):
    # Write your code here
    arr.sort()
    n = len(arr)
    mid = n // 2

    if n % 2 == 0:
        lower_half = arr[:mid]
        upper_half = arr[mid:]
    else:
        lower_half = arr[:mid]
        upper_half = arr[mid + 1:]

    q1 = median(lower_half)
    q2 = median(arr)
    q3 = median(upper_half)

    return [q1, q2, q3]

if __name__ == '__main__':
    n = int(input().strip())
    data = list(map(int, input().rstrip().split()))
    res = quartiles(data)
    for value in res:
        print(value)
