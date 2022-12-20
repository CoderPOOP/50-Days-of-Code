# Link to the Question - https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def mutate_string(string, position, character):
    # Mutations in Python - HackerRank Solution START
    pos = position+1
    Output = string[:position]+character+string[pos:]
    return Output
    # Mutations in Python - HackerRank Solution END

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)