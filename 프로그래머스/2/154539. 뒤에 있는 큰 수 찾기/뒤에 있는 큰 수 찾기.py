def solution(numbers):
    n = len(numbers)
    answer = [-1 for _ in range(n)]
    index = [] # 못찾은 애들의 index
    
    for idx in range(n):
        if not index:
            index.append(idx)
            continue
        
        while index and numbers[index[-1]] < numbers[idx]:
            less_right_num_index = index.pop()
            answer[less_right_num_index] = numbers[idx]
            
        index.append(idx)
    return answer