import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    num = 0
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        answer += 1
        num1 = heapq.heappop(scoville)
        num2 = heapq.heappop(scoville)
        num = num1 + (2 * num2)
        heapq.heappush(scoville,num)
        #print(num1,num2, scoville)
    return answer