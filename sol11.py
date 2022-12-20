# Link to the Question - https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

if __name__ == '__main__':
    N = int(input())
    results = {}
    for i in range(N):
        a = input().split(' ')
        results[a[0]] = [float(x) for x in a[1:]]
    student = input()
    print("%.2f" %(sum(results[student])/len(results[student])))