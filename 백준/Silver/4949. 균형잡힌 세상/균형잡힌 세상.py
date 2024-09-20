import sys

def input():
    return sys.stdin.readline().rstrip()

while True:
    line = input()
    stack = []
    balanced = True

    if line == '.':
        break

    for i in line:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if not stack or stack[-1] != "(":
                balanced = False
                break
            else:
                stack.pop()
        elif i == "]":
            if not stack or stack[-1] != "[":
                balanced = False
                break
            else:
                stack.pop()
    
    if balanced and not stack:
        print("yes")
    else:
        print("no")