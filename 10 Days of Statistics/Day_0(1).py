
from collections import Counter

# Enter your code here. Read input from STDIN. Print output to STDOUT\
n = int(input())
arr = list(map(int, input().split()))

mean = sum(arr) / n

arr.sort()
if n % 2 == 0:
    median = (arr[n//2 - 1] + arr[n//2]) / 2
else:
    median = arr[n//2]

freq = Counter(arr)
max_freq = max(freq.values())
modes = [k for k, v in freq.items() if v == max_freq]
mode = min(modes)

print(f"{mean:.1f}")
print(f"{median:.1f}")
print(mode)