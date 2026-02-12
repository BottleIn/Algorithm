def solution(s):
    answer = ''
    tmp = []
    for x in s:
        tmp.append(x)
    tmp.sort(reverse=True)
    answer = ''.join(tmp)
    return answer