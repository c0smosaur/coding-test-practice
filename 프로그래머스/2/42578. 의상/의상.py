def solution(clothes):
    outfits = {}
    answer = 1
    
    for c in clothes:
        outfits[c[1]] = outfits.get(c[1], 0) + 1
    
    for v in outfits.values():
        answer *= (v+1)
    
    return answer - 1