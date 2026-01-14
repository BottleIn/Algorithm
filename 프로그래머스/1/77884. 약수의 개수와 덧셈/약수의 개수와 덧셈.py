import math

def solution(left, right):
    ans = 0
    for i in range(left, right + 1):
        x = math.isqrt(i)
        if x * x == i:   # 완전제곱수
            ans -= i
        else:
            ans += i
    return ans
