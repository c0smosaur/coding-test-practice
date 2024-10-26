import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
hills = [int(input()) for _ in range(n)]
hills.sort()
min_cost = float('inf')

for low in range(hills[0], hills[-1] - 17 + 1): # 최대높이 - 최소높이
    high = low + 17 # 가능한 최대 높이
    cost = 0
    
    for hill in hills:
        if hill < low:
            cost += (low - hill) ** 2
        elif hill > high:
            cost += (hill - high) ** 2
            
    min_cost = min(min_cost, cost)
           
print(min_cost)