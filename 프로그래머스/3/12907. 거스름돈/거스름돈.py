'''

'''

def solution(n, money):
    answer = 0
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    
    for m in money:
        for x in range(m,n+1):
            dp[x] = (dp[x] + dp[x-m]) % 1000000007
    
        
    
    return dp[n]  % 1000000007