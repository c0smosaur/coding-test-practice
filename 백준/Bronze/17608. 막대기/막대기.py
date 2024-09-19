import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
sticks = [int(input()) for i in range(n)]
highest = 0
answer = 0

for i in range(n-1, -1, -1):
    if sticks[i] > highest:
        answer += 1
        highest = sticks[i]
        
print(answer)
