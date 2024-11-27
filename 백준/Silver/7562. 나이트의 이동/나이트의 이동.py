import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

test_cases = int(input())
hor = [1, 2, 2, 1, -1, -2, -2, -1]
ver = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(start_x, start_y, dest_x, dest_y):
    queue = deque([(start_x, start_y, 0)])
    visited = [[False] * i for _ in range(i)]
    visited[start_y][start_x] = True

    while queue:
        x, y, moves = queue.popleft()

        if x == dest_x and y == dest_y:
            return moves

        for dir in range(8):
            new_x = x + hor[dir]
            new_y = y + ver[dir]

            if 0 <= new_x < i and 0 <= new_y < i and not visited[new_y][new_x]:
                queue.append((new_x, new_y, moves + 1))
                visited[new_y][new_x] = True
    
    return -1

for _ in range(test_cases):
    i = int(input())
    curr_x, curr_y = map(int, input().split())
    dest_x, dest_y = map(int, input().split())

    print(bfs(curr_x, curr_y, dest_x, dest_y))
