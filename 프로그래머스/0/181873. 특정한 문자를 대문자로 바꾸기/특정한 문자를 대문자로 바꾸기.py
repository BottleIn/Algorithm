def solution(my_string, alp):
    answer = ''
    for x in my_string:
        if x == alp:
            x = x.upper()
            answer += x
        else:
            answer += x
    return answer