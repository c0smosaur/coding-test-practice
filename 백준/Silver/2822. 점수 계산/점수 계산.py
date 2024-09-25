import sys

def input():
    return sys.stdin.readline().rstrip()

nums = [(int(input()), i+1) for i in range(8)] # 인덱스를 함께 튜플로 저장
sorted_nums = sorted(nums, reverse=True) # 내림차순으로 정렬
score = sum([num for num, _ in sorted_nums[:5]]) # 큰 순으로 5개 수 합

hi_five = sorted([index for _, index in sorted_nums[:5]]) # 큰 순으로 5개의 수 인덱스 오름차순으로 정렬

print(score)
print(*hi_five)