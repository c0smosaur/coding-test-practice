import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
count = []
maze = [input() for _ in range(n)]
visited = [[False]*m for _ in range(n)]
rl = [0,0,1,-1]
ud = [-1,1,0,0]

def bfs(start_r, start_c):
    queue = deque([(start_r, start_c, 1)])
    visited[start_r][start_c] = True

    while queue:
        r, c, dist = queue.popleft()

        if r == n-1 and c == m-1:
            return dist
        
        for dir in range(4):
            new_r = r + ud[dir]
            new_c = c + rl[dir]

            if 0 <= new_r < n and 0 <= new_c < m and not visited[new_r][new_c] and maze[new_r][new_c] == '1':
                visited[new_r][new_c] = True
                queue.append((new_r, new_c, dist + 1))
    
    return -1

answer = bfs(0,0)
print(answer)