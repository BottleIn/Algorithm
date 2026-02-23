from collections import deque

def solution(x, y, n):
    if x == y: return 0
    
    visited = set()
    visited.add(x)
    
    d = deque([(x, 0)])
    
    while d:
        num, t = d.popleft()
        
        # 다음에 이동 가능한 세 가지 경우
        for next_num in (num + n, num * 2, num * 3):
            if next_num == y:
                return t + 1
            
            # y보다 작고, '처음 방문하는' 숫자일 때만 큐에 삽입
            if next_num < y and next_num not in visited:
                visited.add(next_num)
                d.append((next_num, t + 1))
                
    return -1