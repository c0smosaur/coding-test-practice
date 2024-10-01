import sys

def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
medals = [tuple(map(int, input().split())) for _ in range(n)]
ranks = {}
curr_rank = 1

medals.sort(key = lambda x: (-x[1], -x[2], -x[3])) # 메달 순으로 정렬

for i in range(n):
    if i > 0 and (medals[i][1], medals[i][2], medals[i][3]) != (medals[i-1][1], medals[i-1][2], medals[i-1][3]):
        curr_rank = i + 1
        
    ranks[medals[i][0]] = curr_rank

    if medals[i][0] == k:
        print(curr_rank)