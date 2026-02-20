def solution(s):
    answer = True
    dp = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for x in s:
        if not dp or x == '(':
            dp.append(x)
        if x == ')':
            if dp[-1] == '(':
                dp.pop()
                continue
            else:
                answer = False
                break
    print(dp)
    if dp:
        answer = False
    
    return answer