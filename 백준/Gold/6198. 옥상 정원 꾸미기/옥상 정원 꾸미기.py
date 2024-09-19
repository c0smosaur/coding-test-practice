import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
buildings = []
for _ in range(n):
    buildings.append(int(input()))
    
stack = []
visible = 0

for i in range(n):
    while stack and stack[-1] <= buildings[i]:
        stack.pop()

    visible += len(stack)

    stack.append(buildings[i])

print(visible)