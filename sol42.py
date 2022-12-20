# Link to the Question - https://edabit.com/challenge/8pDH2SRutPoaQghgc

def relation_to_luke(inp):
    myDict = {
        'Darth Vader': 'father',
        'Liea': 'sister',
        'Han': 'brother in law',
        'R2D2': 'droid'
    }
    relation = "Luke, I am your ", myDict[inp]
    return relation

print(relation_to_luke("Liea"))