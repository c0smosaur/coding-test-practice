from collections import deque

def solution(maps):
    m, n = len(maps), len(maps[0]) # 행, 열(y, x)
    queue = deque([(0, 0, 1)]) # (y, x, steps)
    dy = [-1, 1, 0, 0] # 상, 하
    dx = [0, 0, -1, 1] # 좌, 우
    visited = [[False] * n for _ in range(m)] # maps와 동일한 사이즈
    visited[0][0] = True # 시작점은 이미 방문
    
    while queue:
        y, x, steps = queue.popleft()
        
        if y == m-1 and x == n-1: # 목적지 도착했는지 확인
            return steps
        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i] # 이동
            
            if 0 <= ny < m and 0 <= nx < n and not visited[ny][nx] and maps[ny][nx] == 1: # 범위 내 & 방문하지 않은 경로 & 통행 가능 여부
                visited[ny][nx] = True # 방문한 경로에 추가
                queue.append((ny, nx, steps + 1)) # 현재 지점 기록
        
    return -1
    