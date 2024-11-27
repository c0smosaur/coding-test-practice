import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
visited = [False] * (100000 + 1)

def bfs(n, k):
    queue = deque([(n, 0)])
    visited[n] = True

    while queue:
        subin, seconds = queue.popleft()

        if subin == k:
            return seconds

        if 0 <= subin - 1 <= 100000 and not visited[subin - 1]:
            queue.append((subin - 1, seconds + 1))
            visited[subin - 1] = True
        
        if 0 <= subin + 1 <= 100000 and not visited[subin + 1]:
            queue.append((subin + 1, seconds + 1))
            visited[subin + 1] = True
        
        if 0 <= subin * 2 <= 100000 and not visited[subin * 2]:
            queue.append((subin * 2, seconds + 1))
            visited[subin * 2] = True

    return -1

print(bfs(n, k))