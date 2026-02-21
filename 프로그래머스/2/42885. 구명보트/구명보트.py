def solution(people, limit):
    answer = 0
    people.sort()
    
    l = 0
    r = len(people) - 1
    
    while l <= r:
        # 가장 무거운 사람과 가벼운 사람의 합이 limit 이하일 때
        if people[l] + people[r] <= limit:
            l += 1 # 가벼운 사람 태움
        r -= 1     # 무거운 사람은 무조건 태움
        answer += 1
        
    return answer