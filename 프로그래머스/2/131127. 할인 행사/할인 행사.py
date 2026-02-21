from collections import defaultdict, Counter

def solution(want, number, discount):
    answer = 0
    want_dict = {}
    for w, n in zip(want, number):
        want_dict[w] = n
    
    want_counter = Counter(want_dict)
    
    cur_dict = defaultdict(int)
    for x in range(10):
        cur_dict[discount[x]] += 1
    
    l = 0
    r = 10
    
    # len(discount)까지 가야 마지막 10일째 구간을 검사할 수 있습니다.
    while r <= len(discount):
        # [수정 포인트 1] cur_dict를 Counter로 변환 후 빈 Counter를 더해 0인 항목 제거
        if want_counter == (Counter(cur_dict) + Counter()):
            answer += 1
        
        # [수정 포인트 2] r이 범위 내에 있을 때만 갱신
        if r < len(discount):
            cur_dict[discount[l]] -= 1
            cur_dict[discount[r]] += 1
        
        l += 1
        r += 1
    
    return answer