from collections import deque

def solution(arr):
    is_dup = deque()
    for x in arr:
        if len(is_dup) == 0:
            is_dup.append(x)
        else:
            num = is_dup.pop()
            if(num == x):
                is_dup.append(x)
            else:
                is_dup.append(num)
                is_dup.append(x)
    ans = list(is_dup)
    return ans