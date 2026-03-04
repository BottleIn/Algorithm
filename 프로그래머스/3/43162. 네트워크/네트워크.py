from collections import defaultdict,deque
def solution(n, computers):
    answer = 0
    n,m = len(computers), len(computers[0])
    d = defaultdict(list)
    
    
    for x in range(n):
        for y in range(m):
            if x == y:
                continue
            if computers[x][y] == 1:
                d[x].append(y)
    visited = [False for _ in range(n)]
    
    #print(visited)
    
    def bfs(start):
        nonlocal answer
        if visited[start]:
            return
        
        dq = deque([start])
        
        while dq:
            node = dq.popleft()
            visited[node] = True
            
            for neigh in d[node]:
                if not visited[neigh]:
                    dq.append(neigh)
        answer += 1
    
    
    for x in range(n):
        bfs(x)
    
    return answer