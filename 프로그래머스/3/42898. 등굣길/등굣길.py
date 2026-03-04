def solution(m, n, puddles):
    # 1. DP 테이블 초기화 (n+1 행, m+1 열)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # 2. 물웅덩이 표시 (웅덩이는 -1로 표시)
    for x, y in puddles:
        dp[y][x] = -1
    
    # 3. 시작점 설정
    dp[1][1] = 1
    
    # 4. 반복문 (세로 n, 가로 m 순서)
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            # 시작점은 이미 1이므로 건너뜀
            if x == 1 and y == 1:
                continue
            
            # 현재 위치가 물웅덩이라면 값을 0으로 만들고 통과
            if dp[y][x] == -1:
                dp[y][x] = 0
                continue
            
            # 위쪽(y-1)과 왼쪽(x-1)에서 오는 경로를 더함
            # 인덱스 0번 라인은 모두 0이므로 조건문 없이 더해도 안전함
            dp[y][x] = (dp[y-1][x] + dp[y][x-1]) % 1000000007
            
    return dp[n][m]