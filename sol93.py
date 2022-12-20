# Link to the Question - https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true

N = int(input())

countries = set()

for i in range(N):
    countries.add(input())

print(len(countries))