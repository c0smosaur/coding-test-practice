import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
towers = list(map(int, input().split()))
stack = []
answer = []

for _ in range(n):
    while stack:
        if stack[-1][1] > towers[_]:
            answer.append(stack[-1][0]+1)
            break
        else:
            stack.pop()
        
    if not stack:
        answer.append(0)

    stack.append((_, towers[_]))

print(*answer)