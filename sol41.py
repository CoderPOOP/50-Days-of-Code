# Link to the Question - https://edabit.com/challenge/2RtztnzMDdyAj2MD3

def add(num1, num2):
    if num1 or num2 != "":        
        return int(num1) + int(num2)
    else:
        return("Invalid Operation.")

print(add("50", ""))