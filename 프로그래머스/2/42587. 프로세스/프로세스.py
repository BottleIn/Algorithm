from collections import deque

def solution(priorities, location):
    max_num = - 1
    ans = deque()
    sort_prior = sorted(priorities)
    #print(sort_prior)
    idx = 0
    for val in priorities:
        ans.append([idx,val])
        idx += 1
    
    start_time = 1
    # print(ans)
    while ans:
        idx, val = ans.popleft()
        if val < sort_prior[-1]:
            ans.append([idx,val])
            # print(ans)
        else:
            if(location == idx):
                return start_time
            else:
                start_time += 1
                sort_prior.pop()
                # print(ans)
                

# print(solution([1, 1, 9, 1, 1, 1],0))