from collections import deque
def solution(x, y, n):
    answer = 0
    if x == y:
        return 0
    
    visited = [0] * (y+1)
    
    d = deque([(x, 0)]) # 현재값, 연산횟수
    visited[x] = 1
    
    while d:
        curr, count = d.popleft()
        for next_val in (curr+n, curr*2,curr*3):
            if next_val == y:
                return count + 1
                
            if next_val < y and not visited[next_val]:
                visited[next_val] = 1
                d.append((next_val, count + 1))
                
    return -1