import sys
from collections import deque
sys.setrecursionlimit(10000)

def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())

    grid = []
    for _ in range(N):
        line = input().strip().replace(' ', '')  # 혹시 공백이 섞여도 제거
        grid.append([int(ch) for ch in line])

    # 입력만 받는 코드 (출력 없음)
    # print(N, M)
    #print(grid)
    num = 0
    dist = [[0 for _ in range(M)] for _ in range(N)]
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    d = deque()
    d.append((0,0))
    #print(d)
    dist[0][0]=1

    while d:
        curx,cury = d.popleft()
        if curx == N - 1 and cury == M - 1:
            print(dist[curx][cury])
            return

        for i in range(4):
            x = curx + dx[i]
            y = cury + dy[i]

            if 0<=x < N and 0<=y<M:
                if dist[x][y] == 0 and grid[x][y] == 1:
                    d.append((x,y))
                    dist[x][y] = dist[curx][cury] + 1
   
    
    print(num)

if __name__ == "__main__":
    main()
