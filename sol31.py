# Link to the Question - https://www.geeksforgeeks.org/get-yesterdays-date-using-python/

from datetime import date
from datetime import timedelta
 
today = date.today()
print("Today is: ", today)

yesterday = today - timedelta(days = 1)
# here (days = 1) describes the day before
print("Yesterday was: ", yesterday)