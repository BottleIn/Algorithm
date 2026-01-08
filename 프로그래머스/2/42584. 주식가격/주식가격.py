def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []
    
    for idx in range(n):
        
        while stack and prices[idx] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = idx - j
        stack.append(idx)
    
    while stack:
        i = stack.pop()
        answer[i] = n - 1 - i
    
    
    
    return answer