#/bin/python3
n = int(input())
numbers = input().split()

arr = []
for i in range(n):
    arr.append(int(numbers[i]))

for i in range(n-1, -1, -1):
    print(arr[i], end=' ')