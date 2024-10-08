def solution(array, commands):
    answer = []
    for c in commands:
        i, j, k = c[0], c[1], c[2]
        temp = sorted(array[i-1:j])
        answer.append(temp[k-1])
    return answer