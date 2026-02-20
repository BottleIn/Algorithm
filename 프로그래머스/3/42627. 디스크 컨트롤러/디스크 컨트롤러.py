'''
작업의 소요시간(l) 작은거 > 작업의 요청 시각(s) 빠른거 >작업의 번호가 작은 것 (idx)
'''
import heapq

def solution(jobs):
    #요청 시간 순으로 정렬
    jobs.sort()
    
    count = 0      # 처리된 작업 개수
    last_time = -1 # 마지막 작업이 시작된 시간
    now = 0        # 현재 시간
    total_time = 0 # 각 작업의 (종료시간 - 요청시간) 합계
    wait_list = [] # 대기 중인 작업들 (최소 힙)

    while count < len(jobs):
        for job in jobs:
            # 마지막 작업 시작 이후 ~ 현재 시각 사이에 요청된 작업을 힙에 추가
            if last_time < job[0] <= now:
                # (소요시간, 요청시간)
                heapq.heappush(wait_list, [job[1], job[0]])
        
        if wait_list:
            # 3. 대기열 중 소요 시간이 가장 짧은 작업 꺼내기
            duration, request_time = heapq.heappop(wait_list)
            last_time = now
            now += duration
            total_time += (now - request_time) # 종료시간 - 요청시간
            count += 1
        else:
            # 4. 당장 처리할 작업이 없다면 다음 작업 요청 시간으로 이동
            now += 1
            
    return total_time // len(jobs)