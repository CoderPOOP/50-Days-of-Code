# Link to the Question - https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true

from itertools import product
A = input().split()
A = list(map(int,A))
B = input().split()
B = list(map(int, B))
output = list(product(A,B))
for i in output:
    print(i, end = " ");