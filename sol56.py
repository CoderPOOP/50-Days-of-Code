# Link to the Question - https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true&

from itertools import permutations

s,k = input().split()

words = list(permutations(s,int(k)))
words = sorted(words, reverse=False)
for word in words:
    print(*word,sep='')