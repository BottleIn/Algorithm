def solution(n, a, b):
    answer = 0

    while a != b:
        # 1. 다음 라운드 번호로 갱신
        # (a + 1) // 2 와 동일한 논리
        a = (a // 2) + (a % 2)
        b = (b // 2) + (b % 2)
        
        
        answer += 1

    return answer