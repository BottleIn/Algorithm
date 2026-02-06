def solution(stones, k):
    left = 1
    right = 200000000
    
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        
        possible = True 
        for t in stones:
            if t < mid:  # 못 건널 경우
                cnt += 1
            else:       # 건널 수 있으므로 연속성 cnt를 0으로 초기화
                cnt = 0
            
            if cnt >= k: # 빈 돌이 k개 연속이면 못 건넘
                possible = False
                break
        
        if possible:
            left = mid + 1
        else:
            right = mid - 1
            
    return right