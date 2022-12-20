# Link to the Question - https://www.101computing.net/random-odd-and-even-number-functions/

import random

def randomOddNumber(a,b):
  a = a // 2
  b = b // 2 - 1
  number = random.randint(a,b)
  number = (number * 2) + 1
  return number


def randomEvenNumber(a,b):
  a = a // 2
  b = b // 2 - 1
  number = random.randint(a,b)
  number = (number * 2)
  return number
  
oddNumber = randomOddNumber(0,100) 
print("The Random Odd Number you generated is :- " , oddNumber)

evenNumber = randomEvenNumber(0,100) 
print("The Random Even Number you generated is :- " , evenNumber)