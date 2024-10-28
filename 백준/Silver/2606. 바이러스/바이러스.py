import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input()) # 총 노드 수
p = int(input()) # 연결된 쌍의 수
network = [[] for _ in range(n+1)] # 인접 리스트 초기화

for _ in range(p):
    a, b = map(int, input().split())
    network[a].append(b) # 연결 정보 입력
    network[b].append(a)

visited = [False] * (n+1) # 방문 리스트

def dfs(v):
    visited[v] = True # 현재 노드 방문 처리
    count = 1 # 현재 노드에서 시작해 감염된 컴퓨터 수 카운트

    for neighbor in network[v]:
        if not visited[neighbor]:
            count += dfs(neighbor) # 재귀
    return count

infected = dfs(1) - 1 # 1번 컴퓨터 제거

print(infected)