def solution(sizes):
    answer = 0
    max_max = min_max = -1
    
    for x,y in sizes:
        # print(x,y)
        if y > x:    # 무조건 x가 크도록
            t = x
            x = y
            y = t
        if max_max < x:
            max_max = x
        if min_max < y:
            min_max = y
    
    print(max_max,min_max)
    return max_max * min_max