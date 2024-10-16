def dfs(idx, curr_sum, numbers, target):
    if idx == len(numbers):
        return True if curr_sum==target else False
        
    add_path = dfs(idx + 1, curr_sum + numbers[idx], numbers, target)
    sub_path = dfs(idx + 1, curr_sum - numbers[idx], numbers, target)
    
    return add_path + sub_path

def solution(numbers, target):
    idx = 0
    curr_sum = 0
    
    return dfs(idx, curr_sum, numbers, target)