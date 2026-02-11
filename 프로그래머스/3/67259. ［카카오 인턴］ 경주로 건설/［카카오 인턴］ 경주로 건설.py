from collections import deque

def solution(board):
    n = len(board)
    # dist[y][x][direction]: 해당 좌표에 특정 방향으로 도착했을 때의 최소 비용
    # 방향: 0(상), 1(우), 2(하), 3(좌) -> 시계방향
    dist = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]
    
    q = deque()
    
    # 방향 벡터 (상, 우, 하, 좌 순서)
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    
    # 시작점 (0,0)에서 오른쪽(1)과 아래(2)로 출발 가능한지 확인
    if board[0][1] == 0:
        dist[0][1][1] = 100
        q.append((0, 1, 100, 1))
    if board[1][0] == 0:
        dist[1][0][2] = 100
        q.append((1, 0, 100, 2))
        
    while q:
        y, x, cost, d = q.popleft()
        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            
            # 맵 범위 안이고 벽이 아닌 경우
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0:
                # 현재 방향(d)과 다음 이동 방향(i)이 같으면 직선(100), 다르면 코너(600)
                new_cost = cost + (100 if i == d else 600)
                
                # 기존 기록보다 작거나 '같을' 때도 갱신 (중요)
                if new_cost < dist[ny][nx][i]:
                    dist[ny][nx][i] = new_cost
                    q.append((ny, nx, new_cost, i))
                    
    #print(dist[n-1][n-1])
    return min(dist[n-1][n-1])