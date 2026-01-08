def solution(nums):
    max_num = int(len(nums) / 2)
    print(max_num)
    
    a=set(nums)
    print(a)
    
    if len(a)<max_num :
        return len(a)
    else:
        return max_num
    
    return answer