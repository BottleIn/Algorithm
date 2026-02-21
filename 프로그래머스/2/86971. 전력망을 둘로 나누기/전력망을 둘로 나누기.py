from collections import deque, defaultdict
def solution(n, wires):
    graph = defaultdict(list)
    
    # 그래프 노선도
    for x1,x2 in wires:
        graph[x1].append(x2)
        graph[x2].append(x1)
    
    def bfs(start, v1, v2):
        d = deque([start])
        visited  = [False] * (n + 1)
        visited[start] = True
        count = 1   # 얼마나 연결되어 있는지 개수
        while d:
            node = d.popleft()
            for neigh in graph[node]:
                if (node == v1 and neigh == v2) or (node == v2 and neigh == v1):
                    continue
                
                if not visited[neigh]:
                    visited[neigh] = True
                    d.append(neigh)
                    count += 1
        return count
    
    ans = n
    for x1,x2 in wires:
        t1 = bfs(x1,x1,x2)
        t2 = n - t1
        
        ans = min(ans , abs(t1-t2))
    
    return ans