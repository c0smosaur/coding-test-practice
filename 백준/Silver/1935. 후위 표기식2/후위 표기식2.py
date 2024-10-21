import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
expression = input()
val = [int(input()) for _ in range(n)]
stack = []
op = ['+','-','*','/']

for s in expression:
    if s in op:
        b = stack.pop()
        a = stack.pop()
        if s == '+':
            stack.append(a+b)
        elif s == '-':
            stack.append(a-b)
        elif s == '*':
            stack.append(a*b)
        elif s == '/':
            stack.append(a/b)
        
    else:
        stack.append(val[ord(s) - ord('A')])

print(f"{stack.pop():.2f}")