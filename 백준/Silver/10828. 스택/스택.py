import sys

stack = []
num = int(input())

def input():
    return sys.stdin.readline().rstrip()

def push(x):
    stack.append(x)

def pop():
    if not stack:
        print("-1")
    else:
        print(stack.pop())
    
def size():
    print(len(stack))

def empty():
    if not stack:
        print("1")
    else:
        print("0")
        
def top():
    if not stack:
        print("-1")
    else:
        print(stack[-1])

for _ in range(num):
    cmd = list(input().split())
    if cmd[0] == "push":
        push(cmd[1])
    elif cmd[0] == "pop":
        pop()
    elif cmd[0] == "size":
        size()
    elif cmd[0] == "empty":
        empty()
    else:
        top()