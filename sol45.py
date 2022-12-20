# Link to the Question - https://www.hackerrank.com/challenges/whats-your-name/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def print_full_name(a, b):

    # What's Your Name? in Python - HackerRank Solution START
    b = b+"!"
    print("Hello",a, b,"You just delved into python.");
    # What's Your Name? in Python - HackerRank Solution END
    
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)