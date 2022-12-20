# Link to the Question - https://edabit.com/challenge/cXnkmRdxqJrwdsP4n

def dis(price, discount):
    quotient = discount / price
    percent = quotient * 100
    final = price - percent
    return final
    
print('{:.2f}'.format(dis(100, 75)))