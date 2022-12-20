# Link to the Question - https://codewithharry.com/videos/python-practice-programs-in-hindi-9/

SECUREDPASSWORD = (('s', '$'), ('and', '&'), 
            ('a', '@'), ('o', '0'), ('i', '1'),
            ('I', '|'), ('B' or 'b', '8'))

def securePassword(password):
    for a,b in SECUREDPASSWORD:
        password = password.replace(a, b)
    return password
    
if __name__ == "__main__":
    password = input("Enter your password\n")
    password = securePassword(password)
    print(f"Your secure password is {password}")
