import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

m, n, k = map(int, input().split()) # m = 행, n = 열
grid = [[1]*n for _ in range(m)]
visited = [[False]*n for _ in range(m)]
ver = [1,-1,0,0] # up, down, left, right
hor = [0,0,-1,1]
answer = []

def bfs(start_r, start_c):
    queue = deque([(start_r, start_c)])
    visited[start_r][start_c] = True
    count = 1
    
    while queue:
        r, c = queue.popleft()
        
        for dir in range(4):
            new_r = r + ver[dir]
            new_c = c + hor[dir]
            
            if 0 <= new_r < m and 0 <= new_c < n and not visited[new_r][new_c] and grid[new_r][new_c] == 1:
                queue.append((new_r, new_c))
                count += 1
                visited[new_r][new_c] = True
                
    return count

for _ in range(k):
    min_x, min_y, max_x, max_y = map(int, input().split())
    for i in range(min_y, max_y):
        for j in range(min_x, max_x):
            grid[i][j] = 0

for i in range(m):
    for j in range(n):
        if not visited[i][j] and grid[i][j] == 1:
            answer.append(bfs(i, j))

answer.sort()
print(len(answer))
print(*answer)