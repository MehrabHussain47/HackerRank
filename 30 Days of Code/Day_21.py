def print_array(arr):
    for element in arr:
        print(element)

n = int(input())
int_array = [int(input()) for i in range(n)]

n = int(input())
string_array = [input() for i in range(n)]

print_array(int_array)
print_array(string_array)
