# Link to the Qustion - https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

N = int(input())
cmd = []
for i in range(N):
    cmd.append(input().split())

result = []
for i in range(N):
    if cmd[i][0]=='insert':
        cmd.insert(int(cmd[i][1]),int(cmd[i][2]))
    elif cmd[i][0]=='print':
        print(cmd)
    elif cmd[i][0]=='remove':
        cmd.remove(int(cmd[i][1]))
    elif cmd[i][0]=='append':
        cmd.append(int(cmd[i][1]))
    elif cmd[i][0]=='pop':
        cmd.pop()
    elif cmd[i][0]=='sort':
        cmd.sort()
    elif cmd[i][0]=='reverse':
        cmd.reverse()
