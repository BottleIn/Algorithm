def solution(answers):
    answer = []
    a_answers =b_answers=c_answers= 0
    max_num = -1
    b_key = {1:1,3:3,5:4,7:5}
    c_key = {0:3,1:3, 2:1,3:1, 4:2,5:2, 6:4,7:4, 8:5,9:5}
    for idx,x in enumerate(answers):
        if x == idx % 5 + 1:
            a_answers += 1
        
        if idx % 2 == 0 and x == 2:
            b_answers += 1
        
        if idx % 2 != 0:
            if x == b_key[idx % 8]:
                b_answers += 1
            # elif x == answers[idx]:
        
        if x == c_key[idx%10]:
            c_answers +=1
        
    # print(a_answers)
    # print(b_answers)
    # print(c_answers)
    
    m = max(a_answers,b_answers,c_answers)
    
    if m == a_answers:
        answer.append(1)
    if m == b_answers:
        answer.append(2)
    if m == c_answers:
        answer.append(3)
    return answer

# solution([3,1,3,3,3,4,3,5])