#/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#

def bitwiseAnd(N, K):
    # Write your code here
    max_val = 0
    for A in range(1, N):
        for B in range(A + 1, N + 1):
            current = A & B
            if current < K and current > max_val:
                max_val = current
    return max_val

# # Optimized Approach
# def bitwiseAnd(N, K):
#     if (K - 1) | K <= N:
#         return K - 1
#     else:
#         return K - 2
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        fptr.write(str(res) + '\n')

    fptr.close()
