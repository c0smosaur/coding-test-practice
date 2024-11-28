import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

m, n, h = map(int, input().split())
tomatoes = [[input().split() for _ in range(n)] for _ in range(h)]
ripe = deque([(r,c,l,0) for l in range(h) for r in range(n) for c in range(m) if tomatoes[l][r][c]=="1"])
directions = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

def bfs(queue):
    max_days = 0
    
    while queue:
        r, c, l, days = queue.popleft()
        max_days = max(max_days, days)
        
        for dm, dn, dh in directions:
            new_r, new_c, new_l = r + dn, c + dm, l + dh
            if 0 <= new_r < n and 0 <= new_c < m and 0 <= new_l < h and tomatoes[new_l][new_r][new_c] == "0":
                tomatoes[new_l][new_r][new_c] = "1"
                queue.append((new_r, new_c, new_l, days + 1))
                
    return max_days

answer = bfs(ripe)

for i in range(h):
    for j in range(n):
        if "0" in tomatoes[i][j]:
            print(-1)
            exit()

print(answer)