import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
answer = []

for _ in range(n):
    heights = list(map(int, input().split()[1:]))
    temp = []
    steps = 0

    for height in heights:
        p = len(temp)
        for i in range(len(temp)):
            if temp[i] > height:
                p = i
                break

        temp.insert(p, height)
        steps += len(temp) - p - 1

    answer.append(steps)

for j in range(1, n+1):
    print(f"{j} {answer[j-1]}")