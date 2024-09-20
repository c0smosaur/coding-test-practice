import sys

def input():
    return sys.stdin.readline().rstrip()

stack = []
line = input()

for l in line:
    if stack:
        if l == "(":
            stack.append(l)
        else:
            if stack[-1] == "(":
                stack.pop()
            else:
                stack.append(l)
        
    else:
        stack.append(l)
        
print(len(stack))