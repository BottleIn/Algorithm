def solution(numbers, target):
    ans = 0 
    n = len(numbers)
    def dfs(depth, num):
        nonlocal ans
        
        if depth == n:
            if num == target:
                ans += 1
            return 
        dfs(depth+1, num + numbers[depth])
        
        dfs(depth+1, num - numbers[depth])
        
    
    dfs(0,0)  #깊이, 현재 숫자
    return ans