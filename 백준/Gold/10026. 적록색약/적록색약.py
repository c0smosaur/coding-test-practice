import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

hor = [0,0,-1,1]
ver = [-1,1,0,0]

n = int(input())
painting = [list(input().strip()) for _ in range(n)]

def turn_colorblind(painting):
    for i in range(len(painting)):
        for j in range(len(painting[i])):
            if painting[i][j] == "R":
                painting[i][j] = "G"
    return painting

def bfs(r, c, letter, visited):
    queue = deque([(r, c)])
    visited[r][c] = True

    while queue:
        row, col = queue.popleft()
        
        for d in range(4):
            new_r, new_c = row + ver[d], col + hor[d]

            if 0 <= new_r < n and 0 <= new_c < n and not visited[new_r][new_c] and painting[new_r][new_c] == letter:
                queue.append((new_r, new_c))
                visited[new_r][new_c] = True

def count_bfs(painting):
    visited = [[False]*n for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j, painting[i][j], visited)
                count += 1
    
    return count

normal_count = count_bfs(painting)
cb_painting = turn_colorblind(painting)
colorblind_count = count_bfs(cb_painting)

print(normal_count, colorblind_count)