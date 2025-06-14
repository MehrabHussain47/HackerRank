# Enter your code here. Read input from STDIN. Print output to STDOUT.
t = int(input())

for j in range(0, t):
    even = ""
    odd = ""
    str1 = input()
    for i in range(len(str1)):
        if i % 2 == 0:
            even += str1[i]
        else:
            odd += str1[i]
    print(even + " " + odd)