# Link to the Question - https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

from itertools import combinations_with_replacement

io = input().split();
char = sorted(io[0]);
N = int(io[1]);

for i in combinations_with_replacement(char,N):
    print(''.join(i));