def solution(numbers):
    answer = []
    is_sol = [False for _ in range(201)]
    
    for idx, x in enumerate(numbers):
        for y in numbers[idx+1:]:
            if is_sol[x+y] == False : # 아직 없는 경우의 수
                is_sol[x+y] = True
            
    
    for idx,x in enumerate(is_sol):
        if x == True:
            answer.append(idx)
        
    
    return answer