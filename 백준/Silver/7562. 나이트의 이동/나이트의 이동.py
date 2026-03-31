
import sys
from collections import deque
sys.setrecursionlimit(10000)

def main():
    input = sys.stdin.readline

    T = int(input().strip())
    cases = []
    for _ in range(T):
        l = int(input().strip())
        sx, sy = map(int, input().split())
        tx, ty = map(int, input().split())
        cases.append((l, (sx, sy), (tx, ty)))

        
        grid = [[-1 for _ in range(l)] for _ in range(l)]
        # for row in grid:
        #     print(row)
        
        grid[sx][sy] = 0
        d = deque()
        d.append((sx,sy))
        dx = [-2,-1,1,2,2,1,-1,-2]
        dy = [1,2,2,1,-1,-2,-2,-1]

        while d:
            cx,cy = d.popleft()
            if cx == tx and cy == ty:
                print(grid[cx][cy])
                break
            for i in range(8):
                x = cx + dx[i]
                y = cy + dy[i]

                if 0<= x < l and 0<=y < l:
                    if grid[x][y] == -1:
                        grid[x][y] = grid[cx][cy] + 1
                        d.append((x,y))
            
    

    

if __name__ == "__main__":
    main()
