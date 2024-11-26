import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def bfs(f, g, s, u, d):
    visited = [False] * (f + 1) # 1층 ~ f층
    queue = deque([(s, 0)])
    visited[s] = True

    while queue:
        curr_floor, press = queue.popleft()

        if curr_floor == g:
            return press
        
        if curr_floor + u <= f and not visited[curr_floor + u]:
            queue.append((curr_floor + u, press + 1))
            visited[curr_floor + u] = True
        
        if curr_floor - d >= 1 and not visited[curr_floor - d]:
            queue.append((curr_floor - d, press + 1))
            visited[curr_floor - d] = True
    
    return "use the stairs"

f, s, g, u, d = map(int, input().split())
print(bfs(f, g, s, u, d))
