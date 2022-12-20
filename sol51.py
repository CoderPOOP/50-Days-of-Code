# Link to the Question - https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true

import math
import os
import random
import re
import sys

def solve(s):
    s = str(s)
    for i in s[:].split():
        s = s.replace(i,i.capitalize())
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()