from collections import deque
def solution(board):
    answer = 0
    m = len(board)
    n = len(board[0])
    
    for y in range(m):
        for x in range(n):
            if board[y][x] == 'R':
                start = (y,x)
                
                
    #print(start)
    d = deque([(start[0],start[1],0)])
    visited = set([(start[0],start[1])])
    
    while d:
        y,x,dist = d.popleft()
        
        if board[y][x] == 'G':
            return dist
        
        for dy, dx in [(0,1),(1,0),(-1,0),(0,-1)]:
            ny = y
            nx = x
            
            #미끄러지기
            while True:
                nny, nnx = ny + dy, nx + dx
                if 0 <= nny < m and 0 <= nnx < n and board[nny][nnx] != 'D':
                    ny, nx = nny, nnx
                else:
                    break
            
            if (ny, nx) not in visited:
                visited.add((ny,nx))
                d.append((ny,nx,dist + 1))
        
    return -1