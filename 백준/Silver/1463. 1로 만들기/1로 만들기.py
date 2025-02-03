import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
g = [0] * (n + 1)

for i in range(2, n+1):
    g[i] = g[i - 1] + 1

    if i % 2 == 0:
        g[i] = min(g[i], g[i // 2] + 1)

    if i % 3 == 0:
        g[i] = min(g[i], g[i // 3] + 1)

print(g[n])