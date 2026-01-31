import sys
from collections import deque
def main():
    input = sys.stdin.readline

    N = int(input().strip())

    grid = []
    for _ in range(N):
        line = input().strip()
        line = line.replace(' ', '')      # 혹시 "0 1 0 1" 처럼 공백이 섞여도 제거
        grid.append([int(ch) for ch in line])

    # 입력만 받는 코드 (출력 없음)
    # print(N)
    #print(grid)

    dx = [-1,0,1,0]  # 12시 3시 6시 9시
    dy = [0,1,0,-1]

    visited = [[False for _ in range(N)] for _ in range(N)]
    #print(visited)
    ans = []

    for x in range(N):
        for y in range(N):
            if not visited[x][y] and grid[x][y] == 1:
                tmp = 0
                visited[x][y] = True
                tmp += 1
                d = deque([(x,y)])
                while d:
                    curr_x, curr_y = d.popleft() # 1. 현재 기준점을 꺼냄
                    
                    for i in range(4):
                        nx = curr_x + dx[i] # 2. '현재 기준점'에서 상하좌우 계산
                        ny = curr_y + dy[i]
                        
                        if 0 <= nx < N and 0 <= ny < N:
                            if not visited[nx][ny] and grid[nx][ny] == 1:
                                visited[nx][ny] = True # 3. 큐에 넣을 때 즉시 방문 처리!
                                tmp += 1
                                d.append((nx, ny))
                
                ans.append(tmp) # 한 단지가 끝나면 결과 리스트에 추가
    
    ans.sort()
    print(len(ans))
    for x in ans:
        print(x)
if __name__ == "__main__":
    main()
