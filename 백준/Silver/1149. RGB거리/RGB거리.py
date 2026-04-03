import sys

def solution(n, costs):
    answer = 0
    dp = [[0 for _ in range(3)] for _ in range(n)]
    for x in range(3):
        dp[0][x] = costs[0][x]
    
    for y in range(1,n):
        dp[y][0] = min(dp[y-1][1],dp[y-1][2]) + costs[y][0]
        dp[y][1] = min(dp[y-1][0],dp[y-1][2]) + costs[y][1]
        dp[y][2] = min(dp[y-1][1],dp[y-1][0]) + costs[y][2]
    return min(dp[n-1][0],dp[n-1][1],dp[n-1][2])


if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input().strip())
    costs = [list(map(int, input().split())) for _ in range(n)]

    print(solution(n, costs))