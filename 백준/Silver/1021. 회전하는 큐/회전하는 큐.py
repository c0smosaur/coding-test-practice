import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
d = deque(i for i in range(1, n+1))
numbers = map(int, input().split()) # 위치가 아니고 빼낼 숫자 m개가 순서대로
answer = 0

for number in numbers:
    while True:
        if d[0] == number:
            d.popleft()
            break
        else:
            if d.index(number) <= len(d)//2:
                d.rotate(-1)
                answer += 1
            else:
                d.rotate(1)
                answer += 1

print(answer)