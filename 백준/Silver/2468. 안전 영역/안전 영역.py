import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
land = [list(map(int, input().split())) for _ in range(n)]
hor = [0,0,1,-1]
ver = [-1,1,0,0]
min_h = min(map(min, land))
max_h = max(map(max, land))
max_safe_zone = 0

def bfs(start_r, start_c, h):
    queue = deque([(start_r, start_c)])
    visited[start_r][start_c] = True
    
    while queue:
        r, c = queue.popleft()
        
        for dir in range(4):
            new_r = r + ver[dir]
            new_c = c + hor[dir]
            
            if 0 <= new_r < n and 0 <= new_c < n and not visited[new_r][new_c] and land[new_r][new_c] > h:
                queue.append((new_r, new_c))
                visited[new_r][new_c] = True
                
    return 1

for h in range(min_h - 1, max_h + 1):
    visited = [[False]*n for _ in range(n)]
    safe_zone = 0
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and land[i][j] > h:
                bfs(i, j, h)
                safe_zone += 1
                
    max_safe_zone = max(max_safe_zone, safe_zone)
    
print(max_safe_zone)