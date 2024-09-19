import sys

def input():
    return sys.stdin.readline().rstrip()

num = int(input())
stack = []

for _ in range(num):
    cmd = int(input())
    if cmd == 0:
        stack.pop()
    else:
        stack.append(cmd)
        
print(sum(stack))