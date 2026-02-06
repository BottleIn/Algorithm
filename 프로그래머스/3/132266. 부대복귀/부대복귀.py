from collections import defaultdict, deque

def solution(n, roads, sources, destination):
    answer = []
    visited = [-1] * (n+1)  # 0은 나중에 제외
    edge = defaultdict(list)
    
    for x,y in roads:
        edge[x].append(y)
        edge[y].append(x)
    
    
    #print(edge, visited)
    
    visited[destination] = 0
    d = deque()
    d.append(destination)
    
    while d:
        cur_node = d.popleft()
        for neigh in edge[cur_node]:
            if visited[neigh]  == -1:
                visited[neigh] = visited[cur_node] + 1
                d.append(neigh)
    
    for x in sources:
        answer.append(visited[x])
    
    
    return answer