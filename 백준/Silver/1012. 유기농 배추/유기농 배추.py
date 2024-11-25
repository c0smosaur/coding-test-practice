import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def bfs(start_r, start_c):
    queue = deque([(start_r, start_c)])
    visited[start_r][start_c] = True

    while queue:
        r, c = queue.popleft()

        for dir in range(4):
            new_r = r + ud[dir]
            new_c = c + rl[dir]

            if 0 <= new_r < n and 0 <= new_c < m and not visited[new_r][new_c] and patch[new_r][new_c] == 1:
                visited[new_r][new_c] = True
                queue.append((new_r, new_c))

t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    cabbages = [tuple(map(int, input().split())) for _ in range(k)]
    patch = [[0] * m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    count = 0
    rl = [0,0,1,-1]
    ud = [-1,1,0,0]

    for x, y in cabbages:
        patch[x][y] = 1

    for i in range(n):
        for j in range(m):
            if patch[i][j] == 1 and not visited[i][j]:
                bfs(i,j)
                count += 1

    print(count)