from collections import defaultdict, deque

def solution(n, edge):
    answer = 0
    grp = defaultdict(list)
    visited = [0] * (n+1)
    visited[0] = -1
    for u,v in edge:
        grp[u].append(v)
        grp[v].append(u)
    

    node = deque()  # 거쳐갈 순서
    
    node.append(1)
    visited[1] = 1
    
    #length = 2
    
    while node:
        cur = node.popleft()  # 현재 부모 노드 번호
        
        for neigh in grp[cur]:  # 자식 노드 번호 = neigh
            if visited[neigh] == 0:
                visited[neigh] = visited[cur] + 1
                node.append(neigh)
    
    m = max(visited)
    answer = sum(1 for x in visited if x == m)
    return answer
