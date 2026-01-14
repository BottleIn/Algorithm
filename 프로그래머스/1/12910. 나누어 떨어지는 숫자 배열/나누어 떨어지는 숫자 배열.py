def solution(arr, divisor):
    answer = []
    
    for num in arr:
        # print(num, divisor)
        if num % divisor == 0:
            answer.append(num)
    if(len(answer) == 0):
        answer.append(-1)
        return answer
    answer.sort()
    return answer