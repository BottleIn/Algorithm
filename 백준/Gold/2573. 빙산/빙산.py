import sys
from collections import deque

def main():
    input = sys.stdin.readline

    # 1) N, M 입력
    N, M = map(int, input().split())
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    # 2) 빙산 높이 정보 입력
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 주변 0 개수 체크 및 빙산 녹이기 함수
    def melt_iceberg():
        melt_list = []
        for y in range(N):
            for x in range(M):
                if grid[y][x] > 0:
                    zeros = 0
                    for i in range(4):
                        ny, nx = y + dy[i], x + dx[i]
                        if 0 <= ny < N and 0 <= nx < M and grid[ny][nx] == 0:
                            zeros += 1
                    if zeros > 0:
                        melt_list.append((y, x, zeros))
        
        # 찾은 0의 개수만큼 빼기
        for y, x, z in melt_list:
            grid[y][x] = max(0, grid[y][x] - z)

    # 연결된 빙산 덩어리를 탐색하는 BFS
    def bfs(y, x, visited):
        dq = deque([(y, x)])
        visited[y][x] = True

        while dq:
            cy, cx = dq.popleft()
            for i in range(4):
                ny, nx = cy + dy[i], cx + dx[i]
                if 0 <= ny < N and 0 <= nx < M:
                    if grid[ny][nx] > 0 and not visited[ny][nx]:
                        visited[ny][nx] = True
                        dq.append((ny, nx))

    need_year = 0
    while True:
        cnt = 0
        visited = [[False for _ in range(M)] for _ in range(N)]
        
        # 1. 빙산 덩어리 개수 세기
        for y in range(N):
            for x in range(M):
                if grid[y][x] > 0 and not visited[y][x]:
                    bfs(y, x, visited)
                    cnt += 1
        
        # 2. 조건 체크
        if cnt >= 2: # 두 덩어리 이상으로 분리됨
            print(need_year)
            break
        if cnt == 0: # 다 녹을 때까지 분리되지 않음
            print(0)
            break
            
        # 3. 빙산 녹이기 및 연도 증가
        melt_iceberg()
        need_year += 1

if __name__ == "__main__":
    main()