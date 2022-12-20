# Link to the Question - https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def fun1(s):
    for i in range(len(s)):
        if(s[i].isalnum()):
            return True;
            break;
    return False;
        
def fun2(s):
    for i in range(len(s)):
        if(s[i].isalpha()):
            return True;
            break;
    return False;

def fun3(s):
    for i in range(len(s)):
        if(s[i].isdigit()):
            return True;
            break;
    return False;

def fun4(s):
    for i in range(len(s)):
        if(s[i].islower()):
            return True;
            break;
    return False; 
     
def fun5(s):
    for i in range(len(s)):
        if(s[i].isupper()):
            return True;
            break;
    return False;
 

if __name__ == '__main__':
    s = input()
    flagalphanum = fun1(s)
    alphabetical = fun2(s)
    digits = fun3(s)
    lowercase = fun4(s)
    uppercase = fun5(s)
    print(flagalphanum)
    print(alphabetical)
    print(digits)
    print(lowercase)
    print(uppercase)