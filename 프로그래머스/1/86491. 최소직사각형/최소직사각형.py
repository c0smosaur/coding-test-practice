def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][1] > sizes[i][0]:
            sizes[i] = (sizes[i][1], sizes[i][0])

    w = 0
    h = 0
    
    for s in sizes:
        w = max(w, s[0])
        h = max(h, s[1])
        
    return w*h