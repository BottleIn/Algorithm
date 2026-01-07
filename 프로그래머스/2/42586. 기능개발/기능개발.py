import math
from collections import deque


def solution(progresses, speeds):
    ans = []
    answer = deque()
    days = []
    for idx in range(len(progresses)):
        need_day = math.ceil((100 - progresses[idx]) / speeds[idx])
        days.append(need_day)
        # print(need_day)
    # print(days)
    
    
    max_num = -1
    for day in days:
        if len(answer) == 0:
            answer.append(day)
            max_num = day
            print(f'day =  {day}')
        else:
            if max_num >= day:
                answer.append(day)
                print(f'기다리는 day =  {day}')
            else:
                print(f'바뀌는 day =  {day}')
                ans.append(len(answer))
                answer.clear()
                answer.append(day)
                max_num = day
                
    if len(answer) != 0:
        ans.append(len(answer))
        
    return ans