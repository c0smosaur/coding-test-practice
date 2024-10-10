def solution(genres, plays):
    gen_total = {}
    gen_best = {}
    answer = []
    
    for i in range(len(genres)):
        gen = genres[i]
        gen_total[gen] = gen_total.get(gen, 0) + plays[i]
        
        if gen not in gen_best:
            gen_best[gen] = []
            
        gen_best[gen].append((i, plays[i])) # 장르별로 인덱스와 재생수 저장
        
    gen_total = dict(sorted(gen_total.items(), key = lambda item: item[1], reverse=True)) # 총 재생수로 내림차 정렬
    
    for gen in gen_total:
        gb = sorted(gen_best[gen], key = lambda x:(-x[1], x[0]))
        gb = gb[:2]
        answer.extend(song[0] for song in gb)
    
    return answer