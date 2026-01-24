from itertools import permutations, combinations
def solution(n):
    dp = [0,1,2]
    
    for x in range(3,n+1):
        dp.append(dp[x-2] + dp[x-1])
    
    
    return dp[n] % 1234567