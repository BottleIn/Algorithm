import heapq

def solution(n, works):
    answer = 0
    a = []
    for x in works:
        heapq.heappush(a, -x)
    #print(a)
    while n != 0:
        t = heapq.heappop(a)
        if t == 0:
            break
        t += 1
        heapq.heappush(a,t)
        n -= 1
    #print(a)
    num = 0
    for x in a:
        num += (x ** (2))
        #print(num)
    return num