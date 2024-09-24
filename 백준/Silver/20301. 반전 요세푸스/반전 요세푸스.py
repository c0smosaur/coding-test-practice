import sys

def input():
    return sys.stdin.readline().rstrip()

n, k, m = map(int, input().split())

org = [i for i in range(1, n+1)]
stack = []
curr = 0
rev = False

for j in range(n):
    if j != 0 and j % m == 0: # j = 0 일 때 제외
        rev = not rev
    
    if not rev: # 기존 진행 방향, rev = False
        curr = (curr + k - 1) % len(org)
    else: # 반대 방향, rev = True
        curr = (curr - k) % len(org)
        
    stack.append(org.pop(curr))

for s in stack:
    print(s)