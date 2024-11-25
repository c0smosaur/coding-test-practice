import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())

count = 0
rl = [0, 0, -1, 1]
ud = [-1, 1, 0, 0]
papers = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
drawing = deque()

def bfs(start_row, start_col):
    queue = deque([(start_row, start_col)])
    visited[start_row][start_col] = True
    area_size = 1
    
    while queue:
        row, col = queue.popleft()
        
        for d in range(4):
            new_row = row + ud[d]
            new_col = col + rl[d]
            
            if 0 <= new_row < n and 0 <= new_col < m and not visited[new_row][new_col] and papers[new_row][new_col] == 1:
                visited[new_row][new_col] = True
                queue.append((new_row, new_col))
                area_size += 1

    return area_size
                
for i in range(n):
    for j in range(m):
        if papers[i][j] == 1 and not visited[i][j]:
            area = bfs(i, j)
            count += 1
            drawing.append(area)

print(count)
if drawing:
    print(max(drawing))
else:
    print(0)
