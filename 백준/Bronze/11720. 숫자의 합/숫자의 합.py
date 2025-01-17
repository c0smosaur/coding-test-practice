import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
num = input()
answer = 0

for i in range(n):
    j = int(num[i])
    answer+= j

print(answer)