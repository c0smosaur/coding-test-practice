import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
houses = [input() for _ in range(n)]
visited = [[False]*n for _ in range(n)]
hor = [0,0,1,-1]
ver = [-1,1,0,0]
answer = []

def bfs(start_r, start_c):
    queue = deque([(start_r,start_c)])
    visited[start_r][start_c] = True
    count = 1

    while queue:
        r, c= queue.popleft()

        for dir in range(4):
            new_r = r + ver[dir]
            new_c = c + hor[dir]

            if 0 <= new_r < n and 0 <= new_c < n and not visited[new_r][new_c] and houses[new_r][new_c] == '1':
                queue.append((new_r, new_c))
                visited[new_r][new_c] = True
                count += 1
    
    return count

for i in range(n):
    for j in range(n):
        if houses[i][j] == '1' and not visited[i][j]:
            answer.append(bfs(i,j))

print(len(answer))

answer.sort()
for a in answer:
    print(a)