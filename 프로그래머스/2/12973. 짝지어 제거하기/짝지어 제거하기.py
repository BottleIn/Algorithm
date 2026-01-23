def solution(s):
    answer = 0
    ans = []
    tmp = ''
    for x in s:
        if tmp != x:
            tmp = x
            ans.append(x)
        else:
            ans.pop()
            if len(ans) == 0:
                tmp = ''
            else:
                tmp = ans[-1]
            
        
    
    return answer if len(ans) else 1