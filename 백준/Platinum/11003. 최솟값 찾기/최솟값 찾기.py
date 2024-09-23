import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n, l = map(int, input().split())
d = deque() # 인덱스
answer = [] # 최솟값 집합

arr = [int(num) for num in input().split()]

for i in range(n):
    if d and d[0] <= i - l:
        d.popleft()
        
    while d and arr[i] < arr[d[-1]]:
        d.pop()
    
    d.append(i)
    answer.append(arr[d[0]])
    
print(*answer)