import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
hroom = [input() for _ in range(n)]
vroom = [''.join(col) for col in zip(*hroom)]
hcount = 0
vcount = 0

for i in range(n):
    j = 0
    while j < n - 1:
        if hroom[i][j] == "." and hroom[i][j + 1] == ".":
            hcount += 1

            while j < n - 1 and hroom[i][j + 1] == ".": # 방 끝까지 스킵
                j += 1
        j+= 1

for i in range(n):
    j = 0
    while j < n - 1:
        if vroom[i][j] == "." and vroom[i][j + 1] == ".":
            vcount += 1

            while j < n - 1 and vroom[i][j + 1] == ".": # 방 끝까지 스킵
                j += 1
        j+= 1

print(hcount, vcount)