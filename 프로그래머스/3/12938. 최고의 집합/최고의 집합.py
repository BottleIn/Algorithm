def solution(n, s):
    if s < n:
        return [-1]
    
    num = s // n
    rest = s % n
    
    # 1. 모두 몫으로 채웁니다.
    answer = [num] * n
    
    for i in range(rest):
        answer[n - 1 - i] += 1
        
    return answer