def solution(n, k):
    stack = []
    
    while n != 0:
        stack.append(n%k)
        n = n // k
    answer = ''
    for x in stack[::-1]:
        answer += str(x)
    #print(answer)
    nums = answer.split('0')
    #print(nums)
    t = []
    # print(nums)
    for num in nums:
        if not num:
            continue
        num = int(num)
        if num == 1:
            continue
        elif num == 2:
            t.append(num)
            continue
        
        is_prime = True
        for x in range(2, int(num ** (1/2))+1 ):
            if num % x == 0:
                is_prime = False
                break
        
        if is_prime:
            t.append(num)
            
    
    return len(t)