from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for size in course: 
        combination_list = []
        for order in orders:
             # 1. 주문 정렬
            s_order = sorted(order)
            
            # 2. 각 주문에서 size만큼의 조합 생성
            combination_list.extend(combinations(s_order,size))
            
        # 3. 생성된 모든 조합의 빈도수 계산
        combination_counts = Counter(combination_list)
        
    # 4. 빈도수가 2 이상이고, 해당 size에서 가장 많이 주문된 조합 찾기
        if combination_counts:
            max_count = max(combination_counts.values())
            if max_count >= 2:
                for candi, cnt in combination_counts.items():
                    if cnt == max_count:
                        answer.append("".join(candi))
                        

    return sorted(answer)
    