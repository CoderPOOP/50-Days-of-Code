# Link to the Question - https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true

import sys

N = int(input().strip())

if N % 2 != 0:
    print("Weird")
else:
    if N >= 2 and N <= 5:
        print("Not Weird")
    elif N >= 6 and N <= 20:
        print("Weird")
    elif N > 20:
        print("Not Weird")
