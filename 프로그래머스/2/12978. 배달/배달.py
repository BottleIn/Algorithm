from collections import defaultdict, deque

def solution(N, road, K):
    # 1. 그래프 구성: 인접 리스트 방식을 사용하여 가독성과 속도 향상
    # graph[출발지] = [(목적지, 비용), (목적지, 비용), ...]
    graph = defaultdict(list)
    for x, y, cost in road:
        graph[x].append((y, cost))
        graph[y].append((x, cost))
    
    # 2. 최단 거리를 저장할 리스트 (무한대로 초기화)
    visited = [float('inf')] * (N + 1)
    visited[1] = 0  # 1번 마을에서 시작하므로 거리는 0
    
    # 3. BFS를 위한 큐 생성 및 시작 노드 추가
    d = deque([1])
    
    while d:
        cur_node = d.popleft()
        
        # 현재 마을(cur_node)과 연결된 이웃 마을(neigh)들을 확인
        for neigh, cost in graph[cur_node]:
            #  현재 마을을 거쳐서 이웃 마을로 가는 거리가 
            # 이전에 기록된 이웃 마을까지의 거리보다 짧을 경우에만 갱신
            if visited[cur_node] + cost < visited[neigh]:
                visited[neigh] = visited[cur_node] + cost
                # 거리가 갱신된 경우에만 다시 큐에 넣어서 이웃 노드들을 재검사
                d.append(neigh)
    
    
    answer = 0
    for dist in visited:
        if dist <= K:
            answer += 1
            
    return answer