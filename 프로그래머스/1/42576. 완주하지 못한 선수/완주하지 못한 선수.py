from collections import defaultdict

def solution(participant, completion):
    d = defaultdict(int)
    
    for x in participant:
        d[x] += 1
    for y in completion:
        d[y] -= 1
    
    for z in d:
        if d[z] > 0:
            return z
        