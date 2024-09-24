import sys

def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
org = [i for i in range(1,n+1)]
stack = []
curr = 0

for j in range(n):
    curr = (curr + k - 1) % len(org)
    stack.append(org.pop(curr))
    
print("<"+', '.join(map(str,stack))+">")