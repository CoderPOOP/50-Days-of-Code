# Link to the Question - https://edabit.com/challenge/KT8ApJ2EJcLz4K3t2

def getSum(n):
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
   
n = input()