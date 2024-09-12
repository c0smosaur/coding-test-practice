import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
lst = sorted(list(map(int, input().split())))

left = 0
right = n - 1
closest = float('inf') # 초기값
answer = (lst[left], lst[right])

while left < right:
    cur_sum = lst[left] + lst[right]
    if abs(cur_sum) < abs (closest):
        closest = cur_sum
        answer = (lst[left], lst[right])
        
    if cur_sum > 0:
        right -= 1
    else:
        left += 1
        
print(*answer)