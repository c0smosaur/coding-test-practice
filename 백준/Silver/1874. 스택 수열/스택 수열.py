import sys

def input():
    return sys.stdin.readline().rstrip()

num = int(input())
stack = []
answer = []
curr = 1
over = True

for _ in range(num):
    n = int(input())
    while curr <= n:
        stack.append(curr)
        curr += 1
        answer.append("+")
    if stack[-1] == n:
        stack.pop()
        answer.append("-")
    else:
        over = False
    
if over == True:
    for _ in answer:
        print(_)
else:
    print("NO")