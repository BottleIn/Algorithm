import math
from itertools import permutations

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(math.isqrt(n))
    for d in range(3, limit + 1, 2):
        if n % d == 0:
            return False
    return True

def solution(numbers):
    nums = set()
    digits = list(numbers)
    # print(digits)
    for r in range(1, len(digits) + 1):
        for p in permutations(digits, r):
            # print(p)
            nums.add(int(''.join(p)))
    # print(nums)
    answer = 0
    for x in nums:
        if is_prime(x):
            answer += 1
    return answer
