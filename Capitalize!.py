#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s = list(s)
    lst = []
    i = 0
    if s[0].isalpha():
        lst.append(s[0].upper())
        i += 1
    while i < len(s):
        if s[i] == ' ' and s[i + 1].isalpha():
            lst.append(s[i])
            lst.append(s[i + 1].upper())
            i += 2

        else:
            lst.append(s[i])
            i += 1

    return ''.join(lst)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')
    

    fptr.close()
