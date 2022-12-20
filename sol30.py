# Link to the Question - https://www.geeksforgeeks.org/python-program-to-get-current-time/

from datetime import datetime

def time_now():
    time = datetime.now().time()
    return time

print("Current Time =", time_now())