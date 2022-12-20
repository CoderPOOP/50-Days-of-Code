# Link to the Question - https://edabit.com/challenge/2zKetgAJp4WRFXiDT

# Use of len() is prohibited
count = 0
number = int(input("Enter a Number: "))

while (number>0):
    number = number // 10
    count += 1

print("The total number of digits is - ", count)