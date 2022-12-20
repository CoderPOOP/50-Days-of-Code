# Write a program to calculate exponent (x,y) using recursive functions

def exp_rec(x, y):
    if(y == 0):
        return 1
    else:
        return (x * exp_rec(x, y-1))

print(int(exp_rec(2, 5)))