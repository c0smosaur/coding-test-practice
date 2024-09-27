import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
s = []

for _ in range(n):
    cmd = list(map(str, input().split()))

    if cmd[0] == "add":
        num = int(cmd[1])
        if int(cmd[1]) not in s:
            s.append(num)
        
    elif cmd[0] == "remove":
        num = int(cmd[1])
        if int(cmd[1]) in s:
            idx = s.index(num)
            s.pop(idx)
    
    elif cmd[0] == "check":
        num = int(cmd[1])
        print(1 if num in s else 0)

    elif cmd[0] == "toggle":
        num = int(cmd[1])
        if num in s:
            idx = s.index(num)
            s.pop(idx)
        else:
            s.append(num)
    
    elif cmd[0] == "all":
        s = [j for j in range(1,21)]
    
    elif cmd[0] == "empty":
        s = []