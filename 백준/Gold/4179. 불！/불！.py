import sys
from collections import deque

# 빠른 입출력을 위해 sys.stdin 사용
input = sys.stdin.readline

def solve():
    # R: 행(Row), C: 열(Col)
    R, C = map(int, input().split())
    
    maze = []
    jihoon_q = deque()
    fire_q = deque()
    
    # 방문 처리 및 시간 계산용 배열 (-1로 초기화)
    jihoon_dist = [[-1] * C for _ in range(R)]
    # 불의 시간은 비교를 위해 무한대(INF)로 초기화
    fire_dist = [[float('inf')] * C for _ in range(R)]
    
    for r in range(R):
        row = list(input().strip())
        maze.append(row)
        for c in range(C):
            if row[c] == 'J':
                jihoon_q.append((r, c))
                jihoon_dist[r][c] = 0
            elif row[c] == 'F':
                fire_q.append((r, c))
                fire_dist[r][c] = 0

    # 상하좌우 이동 방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 1. 불에 대한 BFS 먼저 실행 (불이 각 좌표에 도달하는 시간 계산)
    while fire_q:
        x, y = fire_q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 범위를 벗어나지 않고, 벽이 아니며, 아직 불이 번지지 않은 곳
            if 0 <= nx < R and 0 <= ny < C:
                if maze[nx][ny] != '#' and fire_dist[nx][ny] == float('inf'):
                    fire_dist[nx][ny] = fire_dist[x][y] + 1
                    fire_q.append((nx, ny))
    
    # 2. 지훈이에 대한 BFS 실행
    while jihoon_q:
        x, y = jihoon_q.popleft()
        
        # 가장자리 도착 시 탈출 성공 (현재 시간 + 1 출력)
        if x == 0 or x == R-1 or y == 0 or y == C-1:
            print(jihoon_dist[x][y] + 1)
            return

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < R and 0 <= ny < C:
                # 벽이 아니고, 지훈이가 방문하지 않은 곳이어야 함
                if maze[nx][ny] != '#' and jihoon_dist[nx][ny] == -1:
                    # 핵심 조건: 지훈이가 도착할 시간 < 불이 도착할 시간
                    if jihoon_dist[x][y] + 1 < fire_dist[nx][ny]:
                        jihoon_dist[nx][ny] = jihoon_dist[x][y] + 1
                        jihoon_q.append((nx, ny))
    
    # 큐가 빌 때까지 탈출 못하면 불가능
    print("IMPOSSIBLE")

if __name__ == "__main__":
    solve()