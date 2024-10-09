def solution(nums):
    limit = len(nums) // 2
    types = len(set(nums))
    
    return min(limit, types)