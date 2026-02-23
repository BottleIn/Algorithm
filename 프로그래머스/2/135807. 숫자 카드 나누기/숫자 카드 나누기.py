from math import gcd
from functools import reduce
def solution(A, B):
    answer = []
    
    def check(a, other):
        for i in other:
            if i%a == 0: return -1
        return a
    
    answer.append(check(reduce(gcd, A), B))
    answer.append(check(reduce(gcd, B), A))
    
    return max(answer) if max(answer)!=-1 else 0