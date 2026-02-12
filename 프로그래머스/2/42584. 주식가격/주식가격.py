from collections import deque
def solution(prices):
    
    n = len(prices)
    answer = [0 for _ in range(n)]
    d = deque()
    #prices = deque(prices)
    t = deque()
    for idx, x in enumerate(prices):
        t.append((x,idx))
    #print(t)
    while t:
        x,idx = t.popleft()
        if not d:
            d.append((x,idx))
        else:
            if x >= d[-1][0]:
                d.append((x,idx))
            else:
                while d and x < d[-1][0]:
                    x_t,idx_t = d.pop()
                    answer[idx_t] = idx - idx_t
                d.append((x,idx))
    #print(d)
    for x,idx in d:
        
        answer[idx] = (n-1) - idx
    #print(answer)
    return answer