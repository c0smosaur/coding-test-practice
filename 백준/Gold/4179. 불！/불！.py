import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

r, c = map(int, input().split())
maze = []
fire_queue = deque()
j_queue = deque()
visited = [[False] * c for _ in range(r)]

hor = [0, 0, -1, 1]
ver = [-1, 1, 0, 0]

for i in range(r):
    line = input()
    maze.append(line)
    
    for j in range(len(line)):
        if line[j] == "J":
            j_queue.append((i, j))
        elif line[j] == "F":
            fire_queue.append((i, j))

def escape():
    time = 0

    while j_queue:
        for _ in range(len(fire_queue)):
            fr, fc = fire_queue.popleft()
            
            for d in range(4):
                nfr, nfc = fr + ver[d], fc + hor[d]
                if 0 <= nfr < r and 0 <= nfc < c and maze[nfr][nfc] == ".":
                    maze[nfr] = maze[nfr][:nfc] + "F" + maze[nfr][nfc+1:] # immutable string
                    fire_queue.append((nfr, nfc))
        
        for _ in range(len(j_queue)):
            jr, jc = j_queue.popleft()
            for d in range(4):
                njr, njc = jr + ver[d], jc + hor[d]
                if njr < 0 or njr >= r or njc < 0 or njc >= c:
                    return time + 1
                
                if maze[njr][njc] == "." and not visited[njr][njc]:
                    visited[njr][njc] = True
                    j_queue.append((njr, njc))
        
        time += 1
    
    return "IMPOSSIBLE"

print(escape())