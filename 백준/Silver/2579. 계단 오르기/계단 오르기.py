import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

if n == 1:
    print(int(input()))
    exit()

stairs = [int(input()) for _ in range(n)]
score = [0] * n
score[0] = stairs[0]

if n > 1:
    score[1] = stairs[0] + stairs[1]
if n > 2:
    score[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

for i in range(3, n):
    score[i] = max(score[i - 2] + stairs[i], score[i - 3] + stairs[i - 1] + stairs[i])

print(score[n-1])