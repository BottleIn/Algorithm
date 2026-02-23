from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    grid = [list(row) for row in maps]

    # S, L, E 위치 찾기
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                S = (i, j)
            elif grid[i][j] == 'L':
                L = (i, j)
            elif grid[i][j] == 'E':
                E = (i, j)

    def bfs(start, target):
        q = deque([start])
        dist = [[-1] * m for _ in range(n)]
        dist[start[0]][start[1]] = 0

        while q:
            x, y = q.popleft()
            if (x, y) == target:
                return dist[x][y]

            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if grid[nx][ny] != 'X' and dist[nx][ny] == -1:
                        dist[nx][ny] = dist[x][y] + 1
                        q.append((nx, ny))
        return -1

    a = bfs(S, L)  # 시작 -> 레버
    if a == -1:
        return -1

    b = bfs(L, E)  # 레버 -> 출구
    if b == -1:
        return -1

    return a + b