def solution(arr1, arr2):
    # print(len(arr1),len(arr1[0]))
    answer = [[0]* len(arr1[0]) for _ in range(len(arr1))]
    for idx2, (x , y) in enumerate(zip(arr1,arr2)):
        for idx, (num1, num2) in enumerate(zip(x,y)):
            answer[idx2][idx] = num1+num2
    return answer