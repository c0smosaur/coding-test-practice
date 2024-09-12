import sys
def input():
    return sys.stdin.readline().rstrip()

n, s = map(int, input().split())
lst = list(map(int, input().split()))

start = 0
cur_sum = 0
min_len = float('inf')
    
for end in range(n):
    cur_sum += lst[end]
    
    while cur_sum >= s:
        min_len = min(min_len, end - start + 1) # 최소 길이 업데이트
        cur_sum -= lst[start] # 이동 결과 합에 반영
        start += 1 # 최소 길이 찾아 이동
        
if min_len == float('inf'):
    print(0)
else:
    print(min_len)