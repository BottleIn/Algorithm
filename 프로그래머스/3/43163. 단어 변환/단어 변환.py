from collections import deque
def solution(begin, target, words):
    answer = 0
    d = deque([(begin, 0)]) # 단어, 횟수
    visited = set([begin]) # 사용여부
    
    while d:
        cur_wrd, cnt = d.popleft()
        
        if cur_wrd == target:
            return cnt
        
        for word in words:
            if 1 == sum( s1!=s2 for s1,s2 in zip(cur_wrd,word)) and word not in visited:
                visited.add(word)
                d.append((word,cnt+1))
    
    return 0