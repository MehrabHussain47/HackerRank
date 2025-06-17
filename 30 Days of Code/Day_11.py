#/bin/python3

import math
import os
import random
import re
import sys

# Solution - 1
# Read the 6x6 2D array
arr = [list(map(int, input().split())) for _ in range(6)]

# Initialize max_sum to a very small number
max_sum = -63  # minimum possible value: 7 * (-9) = -63

# Loop through possible hourglass centers (d)
for i in range(1, 5):       # rows 1 to 4
    for j in range(1, 5):   # cols 1 to 4
        # Calculate hourglass sum
        total = (
            arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] +  # top
            arr[i][j] +                                    # middle
            arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]    # bottom
        )
        # Update max_sum
        if total > max_sum:
            max_sum = total

# Output the maximum hourglass sum
print(max_sum)


# Solution - 2
def solve():
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().split())))

    max_hourglass_sum = -math.inf  # Initialize with negative infinity

    # Iterate through all possible top-left corners of an hourglass
    # An hourglass is 3x3, so we need to stop 2 rows/columns before the end
    for i in range(4):  # Rows
        for j in range(4):  # Columns
            current_hourglass_sum = (
                arr[i][j] + arr[i][j+1] + arr[i][j+2] +  # Top row
                arr[i+1][j+1] +                         # Middle element
                arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]  # Bottom row
            )
            max_hourglass_sum = max(max_hourglass_sum, current_hourglass_sum)

    print(max_hourglass_sum)

if __name__ == '__main__':
    solve()
