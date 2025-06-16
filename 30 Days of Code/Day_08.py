# Enter your code here. Read input from STDIN. Print output to STDOUT.
n = int(input())

my_dict = {}
for i in range(n):
    key, value = input().split()
    my_dict[key] = value

try:
    while True:
        c = input()
        if c in my_dict:
            print(f"{c}={my_dict[c]}")
        else:
            print("Not found")
except EOFError:
    pass