import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
tickets = list(map(int, input().split()))
stack = []
curr = 1

while curr <= n:
    if tickets and tickets[0] == curr:
        tickets.pop(0)
        curr += 1

    elif stack and stack[-1] == curr:
        stack.pop()
        curr += 1
    elif tickets:
        stack.append(tickets.pop(0))
    else:
        break

if not stack and not tickets:
    print("Nice")
else:
    print("Sad")
