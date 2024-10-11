def solution(answers):
    students = [
        [1,2,3,4,5], 
        [2, 1, 2, 3, 2, 4, 2, 5], 
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]    
    scores = []
    
    for student in students:
        score = 0
        for i in range(len(answers)):
            if student[i%len(student)] == answers[i]:
                score += 1
        scores.append(score)
    
    m_score = max(scores)
    answer = [i+1 for i, score in enumerate(scores) if score == m_score]
    
    return answer