import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t):
    p = input()
    n = int(input())
    
    arr = input()
    
    if n == 0:
        d = deque()
    else:
        d = deque(map(int, arr[1:-1].split(',')))
    
    rev = False
    error = False
    
    for cmd in p:
        if cmd == 'R':
            rev = not rev

        elif cmd == 'D':
            if d:
                if rev:
                    d.pop() 
                else:
                    d.popleft()
            else:
                print("error")
                error = True
                break

    if not error:
        if rev:
            d.reverse()
        print('['+','.join(map(str, d))+']')