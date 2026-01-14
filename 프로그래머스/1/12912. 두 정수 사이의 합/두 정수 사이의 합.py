def solution(a, b):
    answer = 0
    big_num = 0
    small_num = 0
    
    if a >=b:
        big_num = a
        small_num = b
    else:
        big_num = b
        small_num = a
    
    
    for num in range(small_num,big_num+1):
        answer += num
    
    return answer