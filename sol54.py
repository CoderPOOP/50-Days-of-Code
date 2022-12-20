# Link to the Question - https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true

import cmath;

num = complex(input())
z = complex(num)

print(cmath.polar(z)[0])
print(cmath.polar(z)[1])