from collections import deque

def solution(priorities, location):
    dq =  deque([(i, p) for i, p in enumerate(priorities)])
    answer = 0
    
    while dq:
        idx, priority = dq.popleft()
        
        if any(p > priority for i, p in dq): 
            dq.append((idx, priority))
        else:
            answer += 1
            if idx == location:
                return answer
    
    
    return answer