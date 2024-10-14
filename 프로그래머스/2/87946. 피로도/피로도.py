import itertools

def solution(k, dungeons):
    combinations = list(itertools.permutations(dungeons))
    answer = 0
    
    for c in combinations:
        curr_stamina = k
        explored = 0
        
        for req_stamina, consumption in c:
            if curr_stamina >= req_stamina:
                curr_stamina -= consumption
                explored += 1
            else:
                break
        
        answer = max(explored, answer)
    
    return answer