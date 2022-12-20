# Link to the Question - https://edabit.com/challenge/ZdnwC3PsXPQTdTiKf

def calculator(num1, operation, num2):
    if operation == "+":
        return num1+num2
    if operation == "-":
        return num1-num2
    if operation == "*" or "×":
        return num1*num2
    if operation == "/":
        if num1 or num2 == 0:
            return "Can't divide by 0!"
        else:
            return num1/num2

print(calculator(67, "+", 3))
print(calculator(67, "-", 3))
print(calculator(67, "*", 3))
print(calculator(67, "/", 3))