import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
cards = deque(range(1, n+1))

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())
    
print(*cards)