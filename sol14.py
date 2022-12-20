# Link to the Question - https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

from itertools import *

K, M = map(int, input().split())
N = []

for _ in range(K):
    N.append(map(int, input().split()[1:]))
    MAX = -1
for i in product(*N):
    MAX = max(sum(map(lambda x: x**2, i))%M, MAX)

print(MAX)