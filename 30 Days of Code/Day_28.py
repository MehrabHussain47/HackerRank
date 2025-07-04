#/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    gmail_users = []

    pattern = re.compile(r'^[a-z.]+@gmail\.com$')
    
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
        if pattern.match(emailID):
            gmail_users.append(firstName)
            
gmail_users.sort()

for name in gmail_users:
    print(name)
