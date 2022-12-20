# Link to the Question - 

#Dictionary 
myDict = {
    'hello': 'Used for greeting',
    'world': 'The place that we live in',
    'god': "Creator of this wortld",
    'trees': 'Lungs of the planet' 
    } 
print(myDict.keys()) 
user_input = input("Enter the word whose meaning you want to know from the words mentioned above?\n")
print("The meaning of this word is :- ", myDict[user_input])