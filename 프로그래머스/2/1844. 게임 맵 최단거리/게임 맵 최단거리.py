from collections import deque

def solution(maps):
    n = len(maps)     # 세로 길이 (행)
    m = len(maps[0])  # 가로 길이 (열)
    
    # 1. 방향 벡터 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 2. 큐 생성 및 시작점 추가 (x, y, 현재까지의 거리)
    queue = deque([(0, 0, 1)])
    
    # 3. 방문 처리용 배열 (0은 미방문, 1은 방문)
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True
    
    while queue:
        x, y, dist = queue.popleft()
        
        # [목적지 도착] BFS는 처음 도달했을 때가 무조건 최단 거리!
        if x == n - 1 and y == m - 1:
            return dist
        
        # 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 맵 범위 확인
            if 0 <= nx < n and 0 <= ny < m:
                # 벽이 아니고(1) 아직 방문하지 않은 경우
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    # 큐에 다음 좌표와 증가된 거리를 함께 삽입
                    queue.append((nx, ny, dist + 1))
                    
    # 모든 탐색이 끝났는데 목적지에 도달하지 못한 경우
    return -1