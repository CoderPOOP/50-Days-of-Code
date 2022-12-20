# Link to the Question - https://codewithharry.com/videos/python-practice-programs-in-hindi-3/

with open('HackerRank/50 days of Code/currencyData.txt') as f:
	lines = f.readlines()

currencyDict = {}
for line in lines:
	parsed = line.split("\t")
	currencyDict[parsed[0]] = parsed[1]

amount = int(input("Enter amount in INR:\n"))
print("Enter the name of the currency you want to convert this amount to? Available Options:\n")
[print(item) for item in currencyDict.keys()]
currency = input("Please enter one of these values: \n")
print(f"{amount} INR is equal to {amount *float(currencyDict[currency])} {currency}")
