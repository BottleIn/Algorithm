import sys
from collections import deque
def main():
    input = sys.stdin.readline

    # 1) n, m
    n, m = map(int, input().split())
    visited = [[False] * m for _ in range(n)]
    # 2) 그림 정보 n줄, 각 줄에 m개
    grid = [list(map(int, input().split())) for _ in range(n)]
    
    max_sq = 0 #최대 사각형 크기
    cnt = 0     #사각형 개수

    def bfs(sy,sx):
        nonlocal max_sq
        dq = deque()
        visited[sy][sx] = True
        dq.append((sy,sx))
        cur_sq = 1
        while dq:
    
            ty,tx = dq.popleft()
            for dy,dx in [(0,1),(1,0),(-1,0),(0,-1)]:
                y = ty + dy
                x = tx + dx
                if 0<= y < n and 0<= x < m and not visited[y][x] and grid[y][x] == 1:
                    dq.append((y,x))
                    visited[y][x] = True
                    cur_sq += 1
                    ##print("A")
        #print('---')
        if cur_sq > max_sq:
            max_sq = cur_sq



    for y in range(n):
        for x in range(m):
            if not visited[y][x] and grid[y][x] == 1:
                cnt += 1
                bfs(y,x)
    print(cnt)
    print(max_sq)

if __name__ == "__main__":
    main()