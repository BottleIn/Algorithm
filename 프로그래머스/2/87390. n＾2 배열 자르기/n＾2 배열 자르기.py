def solution(n, left, right):
    answer = []
    
    for k in range(left, right + 1):
        # 1차원 인덱스 k를 2차원 좌표 (i, j)로 변환
        i = k // n
        j = k % n
        
        # 규칙에 따라 값 계산 (max(i, j) + 1)
        # 0부터 시작하는 인덱스이므로 문제의 예시와 맞추기 위해 +1
        value = max(i, j) + 1
        answer.append(value)
        
    return answer