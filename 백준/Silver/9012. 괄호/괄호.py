import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

for i in range(n):
    vps = input()
    stack = []

    for letter in vps:
        if letter == "(":
            stack.append(letter)
        elif letter == ")":
            if stack:
                stack.pop()
            else:
                stack.append(letter)
                break

    if not stack:
        print("YES")
    else:
        print("NO")