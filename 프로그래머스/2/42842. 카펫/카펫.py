import math

def solution(brown, yellow):
    total = brown + yellow
    
    # 세로(h)는 3 이상이어야 yellow가 존재할 수 있음 (최소 1줄)
    for h in range(3, int(math.isqrt(total)) + 1):
        if total % h == 0:
            w = total // h
            
            # [핵심] 찾은 가로(w), 세로(h)로 계산한 yellow가 입력값과 같은지 확인
            if (w - 2) * (h - 2) == yellow:
                return [w, h]  # 찾으면 바로 리턴 (가로 >= 세로 순서 보장됨)