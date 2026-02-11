def solution(enroll, referral, seller, amount):

    parent = {e: r if r != '-' else 'center' for e, r in zip(enroll, referral)}
    
    #각 인원별 최종 수익
    total_money = {e: 0 for e in enroll}
    
    #판매 기록을 하나씩 처리
    for s, a in zip(seller, amount):
        money = a * 100  # 개당 100원
        curr = s         # 현재 돈을 배분받는 사람
        
        # 추천인을 타고 올라가며 돈을 배분 (센터에 도달하거나 배분할 돈이 0원일 때까지)
        while curr != 'center' and money > 0:
            tax = money // 10         # 상사에게 줄 10% (소수점 버림)
            mine = money - tax        # 내가 가질 나머지 금액
            
            total_money[curr] += mine # 내 장부에 기록
            
            
            curr = parent[curr]
            money = tax
            
            
            if money == 0:
                break
                
    
    return [total_money[e] for e in enroll]