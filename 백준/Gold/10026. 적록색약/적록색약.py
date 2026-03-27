import sys
from collections import deque
def main():
    input = sys.stdin.readline

    # 1) N
    N = int(input().strip())

    # 2) N줄의 그림 (문자열 그대로 보관)
    #grid = [input().strip() for _ in range(N)]
    # 또는 2차원 배열이 편하면:
    grid = [list(input().strip()) for _ in range(N)]

    
    # TODO: 로직 작성
    # print(N)
    #print(grid)

    visited_cansee = [ [False for _ in range(N)] for _ in range(N) ]    #비색약 전용
    visited_cannotsee = [ [False for _ in range(N)] for _ in range(N) ] # 색양 전용

    def bfs(y,x,vis):
        dq = deque()
        vis[y][x] = True
        dq.append((y,x))

        while dq:
            cy, cx = dq.popleft()
            cur_color = grid[cy][cx] #현재 색
            for dy, dx in [(0,1),(0,-1),(1,0),(-1,0)]:
                ny = cy + dy
                nx = cx + dx

                if 0<= ny < N and 0<= nx < N:           # 범위 안에 존재
                    if vis[ny][nx] == False:            # 아직 도달하지 않음
                        if vis is visited_cansee:       # 비색약일 경우 색깔이 같아야 함
                            if cur_color == grid[ny][nx]:
                                dq.append((ny,nx))
                                vis[ny][nx] = True
                        
                        elif vis is visited_cannotsee:  # 색약일 경우 R<->G 교차  or B끼리만
                            if (cur_color == 'R' or cur_color == 'G') and grid[ny][nx] != 'B':
                                dq.append((ny,nx))
                                vis[ny][nx] = True
                            elif grid[ny][nx] == 'B' and cur_color == 'B':
                                dq.append((ny,nx))
                                vis[ny][nx] = True




    
    cansee_cnt = 0
    cannotsee_cnt = 0
    for y in range(N):
        for x in range(N):
            if not visited_cansee[y][x]:
                bfs(y,x,visited_cansee)
                cansee_cnt += 1
            if not visited_cannotsee[y][x]:
                bfs(y,x,visited_cannotsee)
                cannotsee_cnt += 1
    
    print(cansee_cnt, cannotsee_cnt)
    #print(cannotsee_cnt)

if __name__ == "__main__":
    main()