import math
def solution(n):
    answer = -1
    tmp = math.isqrt(n)
    if n == tmp * tmp:
        return (tmp+1)*(tmp+1)
    return answer