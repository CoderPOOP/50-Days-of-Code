# Link to the Question - https://codewithharry.com/videos/python-practice-programs-in-hindi-7/

import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "{}()?<>!@#$%^&*~`;:/"

all = lower + upper + number + symbol
length = 10
password = "".join(random.sample(all, length))
print("The password you generated is : ", password)
