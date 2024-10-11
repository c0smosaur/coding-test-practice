import itertools

def solution(numbers):
    all_combinations = []
    answer = []
    
    for i in range(1, len(numbers)+1):
        all_combinations.extend(itertools.permutations(numbers, i))
        
    combinations = set(int(''.join(c)) for c in all_combinations)
    
    for i in combinations:
        if i < 2:
            continue
        prime = True
        
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                prime = False
                break
                
        if prime:
            answer.append(i)
        
    return len(answer)