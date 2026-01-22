def solution(numbers, target):
    answer = 0
    n = len(numbers)
    
    def dfs(depth,cur_val):
        nonlocal answer
        # print(f"현재 depth {depth}, 현재 값 :  {cur_val}")
        if depth == n:
            if cur_val == target:
                answer += 1
             # print("-----------")
            return
        dfs(depth+1, cur_val+numbers[depth])
        dfs(depth+1, cur_val-numbers[depth])
    
    dfs(0,0)
    return answer