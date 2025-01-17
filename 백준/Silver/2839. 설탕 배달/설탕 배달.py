import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

fives = n // 5

while fives >= 0:
    rem = n - fives * 5
    if rem % 3 == 0:
        threes = rem // 3
        print(fives + threes)
        break

    fives -= 1
else:
    print(-1)