import sys
from collections import deque

sys.setrecursionlimit(10000)


def main():
    input = sys.stdin.readline

    M, N = map(int, input().split())  # M: 가로(열), N: 세로(행)

    box = []
    for _ in range(N):
        row = list(map(int, input().split()))
        box.append(row)

    d = deque()

    # 시작점 (1) 찾기
    for x in range(N):
        for y in range(M):
            if box[x][y] == 1:
                d.append((x,y))
    
    #print(d)
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]


    while d:
        cx,cy = d.popleft() 
        for i in range(4):
            x,y = cx + dx[i], cy+dy[i]
            if 0<= x < N and 0<= y < M:
                if box[x][y] == -1:
                    continue
                if box[x][y] == 0:
                    box[x][y] = box[cx][cy] + 1
                    d.append((x,y))
    # for row in box:
    #     print(row)
    ans = -2
    cantfind = False
    for x in range(N):
        for y in range(M):
            if box[x][y] == 0:
                cantfind = True
            elif box[x][y] > ans: ans = box[x][y]
    if cantfind:
        print(-1)
    else:
        print(ans-1)
    
if __name__ == "__main__":
    main()
