import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n, m, v = map(int, input().split())
matrix = [[0] * (n + 1)  for _ in range(n + 1)]
visited_bfs = [False] * (n + 1)
visited_dfs = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    matrix[a][b], matrix[b][a] = 1, 1

def bfs(v):
    queue = deque([v])
    visited_bfs[v] = True
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for element in range(1, n + 1):
            if matrix[node][element] == 1 and not visited_bfs[element]:
                queue.append(element)
                visited_bfs[element] = True

    return result

def dfs(v, result):
    visited_dfs[v] = True
    result.append(v)

    for element in range(1, n + 1):
        if matrix[v][element] == 1 and not visited_dfs[element]:
            dfs(element, result)

    return result

print(*dfs(v, []))
print(*bfs(v))