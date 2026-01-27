import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
            
        answer += 1
        a1 = heapq.heappop(scoville)
        a2 = heapq.heappop(scoville)
        cur = a1 + (a2 * 2)
        heapq.heappush(scoville, cur)
        
    return answer