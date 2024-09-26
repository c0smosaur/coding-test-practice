import sys
import math

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
answer = 0

if n == 1:
    print(1)

else:
    layer = 1 # 층위
    start = 2 # 시작 방 숫자

    while start <= n:
        start += 6 * layer
        layer += 1

    print(layer)