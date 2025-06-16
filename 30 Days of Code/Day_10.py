#/bin/python3

import math
import os
import random
import re
import sys

if __name__ == "__main__":
    n = int(input().strip())    # decimal number
    res = ''    # binary result

    while n > 0:
        res = str(n % 2) + res
        n //= 2

    # print(res)    # print the binary result
    
    count = 0
    max_count = 0

    for bit in res:
        if bit == "1":
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0

    print(max_count)