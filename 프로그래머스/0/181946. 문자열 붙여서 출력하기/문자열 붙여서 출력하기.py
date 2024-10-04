import sys

def input():
    return sys.stdin.readline().rstrip()

words = list(map(str, input().split()))

print(''.join(words))