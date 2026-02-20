from collections import deque
def solution(priorities, location):
    answer = 0
    process = deque([(i,v) for i,v in enumerate(priorities)])
    # print(process)
    priorities.sort()
    t = 0
    while process:
        idx, val = process.popleft()
        
        if val < priorities[-1]:
            process.append((idx,val))
        else:
            t += 1
            if idx == location:
                return t
        
            priorities.pop()    
    return answer