def solution(n):
    answer = 0
    l = 0
    r = 1
    if n == 1:
        return 1
    nums = []
    for x in range(1,n+1):
        nums.append(x)
    # print(nums)
    
    while l <= r :
        # print(l,r)
        # print(nums[l] , nums[r])
        # print('============')
        tar = 0
        for x in nums[l:r+1]:
            tar += x
        #print(l,r,tar)    
        if tar == n:
            answer += 1
            l += 1
        elif tar < n:
            r += 1
        else:
            l += 1
    
    return answer