def solution(n, arr1, arr2):
    answer = []
    
    for x,y in zip(arr1,arr2):
        tmp = bin(x | y)[2:].zfill(n)
        print(tmp)
        gil = ''
        for num in tmp:
            if num == '1':
                gil += '#'
            else:
                gil += ' '
        answer.append(gil)
    return answer