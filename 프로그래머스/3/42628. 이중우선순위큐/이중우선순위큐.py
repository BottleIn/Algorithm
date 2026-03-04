import heapq

def solution(operations):
    min_h, max_h = [], []
    # visited[i] = i번째로 'I' 했던 숫자가 아직 살아있는가?
    visited = [False] * 1000001 
    
    for i, op in enumerate(operations):
        cmd, val = op.split()
        num = int(val)
        
        if cmd == 'I':
            heapq.heappush(min_h, (num, i))
            heapq.heappush(max_h, (-num, i))
            visited[i] = True # i번째 숫자 들어왔다고 표시!
            
        elif num == 1: # 최댓값 삭제
            # 1. 쓰레기 청소 (이미 딴데서 삭제된 애들 버리기)
            while max_h and not visited[max_h[0][1]]:
                heapq.heappop(max_h)
            # 2. 진짜 삭제
            if max_h:
                _, idx = heapq.heappop(max_h)
                visited[idx] = False
                
        else: # 최솟값 삭제
            while min_h and not visited[min_h[0][1]]:
                heapq.heappop(min_h)
            if min_h:
                _, idx = heapq.heappop(min_h)
                visited[idx] = False

    # 마지막으로 한 번 더 청소 (최종 결과 뽑기 전)
    while min_h and not visited[min_h[0][1]]: heapq.heappop(min_h)
    while max_h and not visited[max_h[0][1]]: heapq.heappop(max_h)

    if not min_h:
        return [0, 0]
    return [-max_h[0][0], min_h[0][0]]