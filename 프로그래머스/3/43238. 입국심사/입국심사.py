def solution(n, times):
    answer = 0
    l = 1
    r = 1000000000000000000 
    min_time = 1000000000000000000
    while l<=r:
        can = 0
        mid = (l+r) // 2
        for x in times:
            can += (mid//x)
        
        if can >= n:
            answer = mid
            r = mid - 1
        else:
            l = mid + 1
        #min_time = min(min_time, can)
        #print(answer)
    
    
    
    return answer