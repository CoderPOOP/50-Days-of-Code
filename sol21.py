# Link to the Question - https://codewithharry.com/videos/basic-python-programs-2/

number = int(input("Enter the number: "))
numb = number
reverse = 0
 
while (number > 0):
    dig = number % 10
    reverse = reverse * 10 + dig
    number = number // 10

if numb == reverse:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")  