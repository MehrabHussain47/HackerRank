#/bin/python3

def multiplication_table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

n = int(input())
multiplication_table(n)