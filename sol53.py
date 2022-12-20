# Link to the Question - https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

def print_formatted(number):
    l1 = len(bin(number)[2:])
   
    for i in range(1,number+1):
        print(str(i).rjust(l1,' '),end=" ")
        print(oct(i)[2:].rjust(l1,' '),end=" ")
        print(((hex(i)[2:]).upper()).rjust(l1,' '),end=" ")
        print(bin(i)[2:].rjust(l1,' '),end=" ")
        print("")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)