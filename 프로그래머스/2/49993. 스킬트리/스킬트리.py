def solution(skill, skill_trees):
    answer = 0
    able_skill = {}
    for x in skill:
        able_skill[x] = 1
    
    a = len(skill)
    

    for candi in skill_trees:
        curLen = len(candi)
        b = 0
        is_able = 0
        for x in candi:
            #print(x)
            if x not in able_skill:
                is_able +=1
                continue
            if x != skill[b]:
                break
            else:
                if b +1 < a:
                    b += 1
                #print(b)
                is_able +=1
        # print('===')
        # print(is_able, curLen)
        if is_able == curLen:
            print(candi)
            answer += 1
        
    return answer

# print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))