import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

m, n = map(int, input().split())
tomatoes = [input().split() for _ in range(n)]
ripe = deque([(r,c,0) for r in range(n) for c in range(m) if tomatoes[r][c] == '1'])
hor = [0,0,1,-1]
ver = [-1,1,0,0]

def bfs(queue):
    max_days = 0
    
    while queue:
        r, c, days = queue.popleft()
        max_days = max(days, max_days)

        for dir in range(4):
            new_r = r + ver[dir]
            new_c = c + hor[dir]

            if 0 <= new_r < n and 0 <= new_c < m and tomatoes[new_r][new_c] == '0':
                queue.append((new_r, new_c, days + 1))
                tomatoes[new_r][new_c] = '1'

    return max_days

answer = bfs(ripe)

for r in range(n):
    for c in range(m):
        if tomatoes[r][c] == '0':
            print(-1)
            exit()

print(answer)