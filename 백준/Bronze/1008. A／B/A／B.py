import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

a, b = map(int, input().split())
print(a/b)