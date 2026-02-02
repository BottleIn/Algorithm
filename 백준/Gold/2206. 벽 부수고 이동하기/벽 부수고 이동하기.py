import sys
from collections import deque

def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())

    grid = []
    for _ in range(N):
        line = input().strip()
        grid.append([int(ch) for ch in line])

    # [수정 1] 방문 기록을 3차원으로 변경: [행][열][벽부수기여부(0 or 1)]
    # road[x][y][0]: 벽을 안 부수고 온 거리
    # road[x][y][1]: 벽을 부수고 온 거리
    road = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    
    # 시작점 초기화 (벽 안 부순 상태 0)
    road[0][0][0] = 1

    d = deque()
    # (x, y, 벽부수기 사용 여부)
    d.append((0, 0, 0)) 
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while d:
        cx, cy, broken = d.popleft()

        # 도착지점 확인
        if cx == N - 1 and cy == M - 1:
            print(road[cx][cy][broken])
            return

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                # 1. 다음 칸이 '길(0)'인 경우
                # 현재 상태(broken)를 그대로 유지하며 이동
                if grid[nx][ny] == 0 and road[nx][ny][broken] == 0:
                    road[nx][ny][broken] = road[cx][cy][broken] + 1
                    d.append((nx, ny, broken))
                
                # 2. 다음 칸이 '벽(1)'인 경우
                # 아직 벽을 부순 적이 없다면(broken == 0), 벽을 부수고(1) 이동
                elif grid[nx][ny] == 1 and broken == 0 and road[nx][ny][1] == 0:
                    road[nx][ny][1] = road[cx][cy][broken] + 1
                    d.append((nx, ny, 1))

    # 도착하지 못한 경우
    print(-1)

if __name__ == "__main__":
    main()