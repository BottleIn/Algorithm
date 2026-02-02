import sys
sys.setrecursionlimit(10000)
def main():
    input = sys.stdin.readline

    T = int(input().strip())
    cases = []
    for _ in range(T):
        M, N, K = map(int, input().split())
        pos = []
        for _ in range(K):
            x, y = map(int, input().split())
            pos.append((x, y))
        cases.append((M, N, K, pos))

        grid = [[0 for _ in range(N)] for _ in range(M)]
        
        for x,y in pos:
            grid[x][y] = 1
        
        #테스트
        # for row in grid:
        #     print(row)
        dx = [-1,0,1,0] # 시계방향
        dy = [0,1,0,-1]
        visited = [[False for _ in range(N)] for _ in range(M)]
        ans = 0
        # for row in visited:
        #     print(row)
        def dfs(x,y,dep):
            nonlocal ans
            if not visited[x][y] and grid[x][y] == 1:
                #print(x,y,dep)
                if dep == 1:
                    ans += 1
                    #print(ans)
                visited[x][y] = True
                for i in range(4):
                    tx = x + dx[i]
                    ty = y + dy[i]
                    if 0<= tx < M and 0 <= ty < N:
                        dfs(tx,ty, dep+1)
            
            return
        
        for x,y in pos:
            dep = 1
            dfs(x,y,dep)
        print(ans)
        #print(ans)





if __name__ == "__main__":
    main()
