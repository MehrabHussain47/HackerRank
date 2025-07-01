import math
# Enter your code here. Read input from STDIN. Print output to STDOUT

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

T = int(input())
for _ in range(T):
    n = int(input())
    print("Prime" if is_prime(n) else "Not prime")
else:
    print("False")