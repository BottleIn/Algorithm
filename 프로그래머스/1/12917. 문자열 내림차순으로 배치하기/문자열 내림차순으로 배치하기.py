def solution(s):
    answer = ''
    print(s)
    a = list(s)
    a.sort(reverse=True)
    print(a)
    answer = ''.join(a)
# print('A')
    return answer