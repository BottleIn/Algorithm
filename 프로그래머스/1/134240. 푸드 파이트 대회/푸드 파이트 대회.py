def solution(food):
    answer = ''
    front = []
    back = []
    
    for idx, num in enumerate(food[1:]) :
        use_num = int(num/2)
        # print(use_num)
        for _ in range(use_num):
            front.append(idx+1)
            back.append(idx+1)
        
        #print(front,back)
    
    front.append(0)
    back.sort(reverse=True)
    for x in front+back :
        answer += str(x)
    return answer