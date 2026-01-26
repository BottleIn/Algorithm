from collections import deque

def is_valid(x,y):
    if abs(x-y) != 1:
        return False
    a = min(x,y)
    b = max(x,y)
    if a % 2 != 0 and b % 2 == 0:
        return True
    return False



def solution(n,a,b):
    answer = 1
    d = deque([a,b])
    # is_cor = is_valid(d[0],d[1])
    # print(is_cor)
    
    # print(is_valid(d[0],d[1]))
    # print(abs(d[0]-d[1]))
    
    while not is_valid(d[0],d[1]) or abs(d[0]-d[1]) != 1:
        for x in list(d): 
            if x % 2 == 0:
                d.append(x // 2)
            else:
                d.append((x + 1) // 2)
        for _ in range(2):
            d.popleft()
        answer += 1
    return answer


# print(is_valid(2,3))
# print(is_valid(1,2))
# print(solution(8,2,3))