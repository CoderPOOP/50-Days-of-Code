# Check if a String Contains only Identical Characters

def is_identical(s):
    a_set = set(s)
    return (len(a_set)) == 1