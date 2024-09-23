import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

d = deque()
n = int(input())

for i in range(n):
    cmd = input().split()
    if cmd[0] == "push":
        d.append(cmd[-1])
    elif cmd[0] == "pop":
        print(d.popleft() if d else -1)
    elif cmd[0] == "size":
        print(len(d))
    elif cmd[0] == "empty":
        print(0 if d else 1)
    elif cmd[0] == "front":
        print(d[0] if d else -1)
    elif cmd[0] == "back":
        print(d[-1] if d else -1)