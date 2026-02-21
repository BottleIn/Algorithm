from collections import deque
def solution(maps):
    answer = 0
    n = len(maps)     # 세로 길이 (행)
    m = len(maps[0])  # 가로 길이 (열)
    
    dx = [0,1,0,-1]  
    dy = [1,0,-1,0]
    
    visited = [ [False for _ in range(m)] for _ in range(n)]
    # print(visited)
    
    d = deque([(0,0,1)])
    visited[0][0] = True
    
    while d:
        x, y, dist = d.popleft()
        
        if x == n-1 and y == m-1:
            return dist
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    d.append((nx, ny, dist + 1))
    
    return -1