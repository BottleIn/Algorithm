def solution(arr):
    answer = []
    if(len(arr) == 1):
        return [-1]
    
    tmp = sorted(arr,reverse=True)
    # print(tmp)
    a = tmp.pop()
    arr.remove(a)
    answer = arr
    
    return answer