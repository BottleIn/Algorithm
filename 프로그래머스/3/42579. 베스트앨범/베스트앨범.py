from collections import defaultdict,Counter

def solution(genres, plays):
    d = defaultdict(list)
    answer = []
    t = defaultdict(int)
    for g,(idx,p) in zip(genres,enumerate(plays)):
        d[g].append((p,idx))
        t[g] += p
    
    
    t = sorted(t.items(), key=lambda x: x[1], reverse=True)
    
    for x in d:
        d[x].sort(key=lambda y: (-y[0], y[1]))
    
    
    for genre, _ in t:
        for p, idx in d[genre][:2]:
            answer.append(idx)

    return answer