from collections import defaultdict

def solution(participant, completion):
    answer = ''
    dict = defaultdict(int)
    # set_participant = set(participant)
    for name in participant:
        dict[name] += 1
    
    for name in completion:
        dict[name] -= 1
    ans = ''
    for x in dict:
        if dict[x] > 0:
            return x
    
    return 