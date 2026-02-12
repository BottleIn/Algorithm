def solution(left, right):
    answer = 0
    for num in range(left,right+1):
        tmp = []
        for x in range(1, int(num ** (1/2) + 1)):
            if num % x == 0:
                tmp.append(x)
                if (x != num//x):
                    tmp.append(num//x)
        #print(tmp)
        n = len(tmp)
        if n % 2 == 0:
            answer +=  num
        else:
            answer -= num
    return answer