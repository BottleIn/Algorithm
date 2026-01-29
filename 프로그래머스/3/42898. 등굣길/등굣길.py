'''
n*m 인데 1,1 부터 시작해야 함
'''

def solution(m, n, puddles):
    answer = 0
    dp = [ [0 for _ in range(m+1)] for _ in range(n+1)]
    
    
    # for x in range(1,m+1):
    #     dp[1][x] = 1
    # for x in range(1,n+1):
    #     dp[x][1] = 1
    dp[1][1] = 1
    
    for x,y in puddles:
        dp[y][x] = -1
        
    
    
    for x in range(1,m+1):
        for y in range(1,n+1):
            # if x == y == 1: continue
            if dp[y][x] == 0:
                if dp[y][x-1] == -1 and dp[y-1][x] == -1:
                    dp[y][x] = 0
                    continue
                if dp[y-1][x] != -1:
                    dp[y][x] += dp[y-1][x] % 1000000007
                if dp[y][x-1] != -1:
                    dp[y][x] += dp[y][x-1] % 1000000007
    
    for row in dp:
        print(row)
    
    
    
    return dp[n][m] % 1000000007