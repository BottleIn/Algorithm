from collections import deque
def solution(maps):
    answer = []
    m = len(maps)
    n = len(maps[0])
    
    visited = [[0 for _ in range(n)] for _ in range(m) ]
    
    for y in range(m):
        for x in range(n):
            if maps[y][x] == 'X':
                visited[y][x] = -1
    #print(visited)    

    '''
    'x'표시((-1) 이거나 이미 0이 아닌 숫자로 채워진 경우는 못간다.
    더이상 갈곳이 없을 때 answer를 추가한다
    '''
    
    def bfs(y,x):
        d = deque([(y,x)])
        total_sum = int(maps[y][x])
        visited[y][x] = 1
        while d:
            cy,cx = d.popleft()
            # visited[cy][cx] += cnum
            
            for dy, dx in [(0,1),(0,-1),(1,0),(-1,0)]:
                ny = dy + cy
                nx = dx + cx
                
                if 0 <= ny < m and 0 <= nx < n:
                    if visited[ny][nx] == 0:
                        visited[ny][nx] = 1
                        total_sum += int(maps[ny][nx])
                        d.append((ny, nx))
        return total_sum
    
    
    
    
    
    # 실행
    for y in range(m):
        for x in range(n):
            if visited[y][x] == 0:
                num = bfs(y,x)
                answer.append(num)
    
    return sorted(answer) if len(answer) else [-1]