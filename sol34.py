# Link to the Question - https://codewithharry.com/videos/basic-python-programs-3/
# Link to the Question - https://edabit.com/challenge/FF6kYPHdAcJnoosr5

def factorial_calculator():
    number = int(input("Enter the number: "))
    factorial = 1
    if (number < 0 or number == 1):
        print("1")
    else:
        for i in range(1, number+1):
           factorial = factorial * i
        factorial_num = "The factorial is: ", factorial
        return factorial_num

print(factorial_calculator())