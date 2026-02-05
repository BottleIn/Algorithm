from collections import defaultdict, deque
import sys

def solution(begin, target, words):
    if target not in words:
        return 0
    
    ans = 0
    d = deque()
    d.append(begin)
    visited = {}
    
    visited[begin] = 0
    
    for wrd in words:
        visited[wrd] = 0
    # print(visited)
    # return 0
    
    while d:
        check_word = d.popleft()
        if check_word == target:
            ans = visited[check_word]
            break
        
        for wrd in words:
            if visited[wrd] == 0:
                #print(check_word, wrd)
                different_word_num = sum(c1 != c2 for c1, c2 in zip(check_word, wrd))
                if different_word_num == 1:
                    visited[wrd] = visited[check_word] + 1
                    d.append(wrd)
    #print(visited)
    return ans