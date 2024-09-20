import sys

def input():
    return sys.stdin.readline().rstrip()

stack = []
nums = []
line = input()

for i in line:
    if i.isdigit():
        stack.append(int(i))
    else:
        a = stack.pop()
        b = stack.pop()
        if i == '+':
            stack.append(a+b)
        elif i == '-':
            stack.append(b-a)
        elif i == '*':
            stack.append(b*a)
        elif i == '/':
            stack.append(b//a)

print(*stack)