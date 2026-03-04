'''
배출 우선순위 : 소요시간(l), 요청 시각(s), 작업 번호(idx)
'''
import heapq
def solution(jobs):
    answer = 0
    jobs_order = []
    
    for idx, (s, l) in enumerate(jobs):
        jobs_order.append((s,l,idx))
    
    jobs_order.sort()  # 요청 시각 순서에 따라 정렬
    n = len(jobs_order) # 요청 일 개수
    
    now = 0 # 현재 시각
    last_end_time = -1 # 이전 일이 시작한 시간
    count = 0 # 처리한 jobs 개수  -> n개 될 때까지 
    total = 0 # 전체 처리한 시간
    d = [] # 대기 큐
    
    #시간을 증가시켜가며 비교
    while count < n:            #요청된 일을 다 처리할 때 까지
        for jobs in jobs_order: # 처리할 수 있는 일들인지 확인
            if last_end_time < jobs[0] <= now:
                heapq.heappush(d, [jobs[1],jobs[0],jobs[2]])        
        
        
        if d:  #제일 짧은 것만 나오게
            duration, request_time, idx = heapq.heappop(d)
            last_end_time = now
            now += duration
            total += (now - request_time)
            count += 1
        
        else:
            now += 1
        
    
    
    return total // n