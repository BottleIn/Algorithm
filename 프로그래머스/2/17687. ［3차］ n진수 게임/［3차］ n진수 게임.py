def solution(n, t, m, p):
    answer = ''
    total = t * m
    tmp = [0]
    start = 1
    dic = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    
    while total > 0:
        cur = start
        tp = []
        while cur != 0:
            tp.append(cur%n)
            total -= 1
            cur = cur // n
        tp.reverse()
        for x in tp:
            tmp.append(x)
        start += 1
    
    
    #print(tmp)
    for idx,x in enumerate(tmp):
        if t <= 0:
            break
        if (idx % m) + 1== p:
            if x in dic:
                answer += dic[x]
            else:
                answer += (str(x))
            t -= 1
    return answer