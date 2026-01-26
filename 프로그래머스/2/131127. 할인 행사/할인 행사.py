def solution(want, number, discount):
    answer = 0
    target = {w: n for w, n in zip(want, number)}
    
    
    for i in range(len(discount) - 9):
        
        current_10_days = discount[i : i + 10]
        
        current_dic = {}
        for item in current_10_days:
            if item in target:
                current_dic[item] = current_dic.get(item, 0) + 1
        
        # 5. 목표(target)와 현재(current_dic)가 같은지 비교
        if current_dic == target:
            answer += 1
    return answer