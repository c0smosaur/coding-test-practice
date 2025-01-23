import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

t = int(input())
hor = [0, 0, -1, 1]
ver = [-1, 1, 0, 0]

def escape(w, h, maze, visited, f_queue, s_queue):
    time = 0

    while s_queue:
        
        for i in range(len(f_queue)):
            fr, fc = f_queue.popleft()
            
            for d in range(4):
                nfr, nfc = fr + ver[d], fc + hor[d]

                if 0 <= nfr < h and 0 <= nfc < w and maze[nfr][nfc] == ".":
                    maze[nfr] = maze[nfr][:nfc] + "*" + maze[nfr][nfc+1:]
                    f_queue.append((nfr, nfc))

        for j in range(len(s_queue)):
            sr, sc = s_queue.popleft()

            for d in range(4):
                nsr, nsc = sr + ver[d], sc + hor[d]

                if 0 > nsr or nsr >= h or 0 > nsc or nsc >= w:
                    return time + 1
                
                if maze[nsr][nsc] == "." and not visited[nsr][nsc]:
                    s_queue.append((nsr, nsc))
                    visited[nsr][nsc] = True

        time += 1
    
    return "IMPOSSIBLE"

for _ in range(t):
    w, h = map(int, input().split())
    maze = []
    visited = [[False] * w for _ in range(h)]
    f_queue = deque()
    s_queue = deque()

    for i in range(h):
        line = input()
        maze.append(line)
        for j in range(w):
            if line[j] == "*":
                f_queue.append((i, j))
            elif line[j] == "@":
                s_queue.append((i, j))
    
    print(escape(w, h, maze, visited, f_queue, s_queue))