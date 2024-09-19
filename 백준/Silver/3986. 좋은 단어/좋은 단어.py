import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input()) 
answer = 0 

for i in range(n):
    word = list(input())
    stack = []

    for j in word:
        if stack and stack[-1] == j:
            stack.pop()
        else:
            stack.append(j)

    if len(stack) == 0:
        answer += 1

print(answer)