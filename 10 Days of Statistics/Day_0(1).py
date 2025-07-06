import statistics

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
number = input().split()
arr =[]
for i in range(n):
    arr.append(int(number[i]))

mean = statistics.mean(arr)
median = statistics.median(arr)

from collections import Counter

freq = Counter(arr)
freq_values = list(freq.values())

if all(val == freq_values[0] for val in freq_values):
    mode = min(arr)
else:
    mode = statistics.mode(arr)

print(mean)
print(median)
print(mode)