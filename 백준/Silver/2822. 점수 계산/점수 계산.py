import sys

def input():
    return sys.stdin.readline().rstrip()

hi_five = []
nums = [int(input()) for i in range(8)]
sorted_nums = sorted(nums)
score = 0

for j in sorted_nums[3:]:
    score += j
    hi_five.append(nums.index(j)+1)

hi_five.sort()

print(score)
print(*hi_five)