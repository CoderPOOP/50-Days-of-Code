# Link to the Question - https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

lis=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    
    lis.append([name,score])

lis.sort(key=lambda lis:lis[1])

second_lowest=[]
for i in range(len(lis)):
    if lis[i][1]!=lis[0][1]:
        second_lowest.append(lis[i][0])
        for j in range(i+1,len(lis)):
            if lis[j][1]==lis[i][1]:
                second_lowest.append(lis[j][0])
            else:
                break
        break
