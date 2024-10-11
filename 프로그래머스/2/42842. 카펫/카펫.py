def solution(brown, yellow):
    total = brown + yellow
    
    for v in range(3, total//2+1):
        if total % v == 0:
            h = total // v
            if (h-2)*(v-2) == yellow:
                return [h, v]