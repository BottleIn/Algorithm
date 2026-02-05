from collections import defaultdict,deque

def solution(n, results):
    answer = 0
    win_graph = defaultdict(list)
    lose_graph = defaultdict(list)
    for u,v in results:
        win_graph[u].append(v)
        lose_graph[v].append(u)
    # print(win_graph)
    # print(lose_graph)
    
    def bfs(start, graph):
        q = deque([start])
        visited = [False] * (n + 1)
        visited[start] = True
        count = 0
        
        
        while q:
            cur = q.popleft()
            for neighbor in graph[cur]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)
                    count += 1 # 도달 가능한 사람 수 증가
        return count
    
    for i in range(1,n+1):
        win_count = bfs(i, win_graph)   # 내가 이긴 사람 수 (간접 포함)
        lose_count = bfs(i, lose_graph) # 나한테 이긴 사람 수 (간접 포함)
        
        if win_count + lose_count == n - 1:
            answer += 1
    return answer