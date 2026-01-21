from collections import defaultdict, deque
import sys

def solution(n, wires):
    answer = n
    dict = defaultdict(list)
    
    for x,y in wires:
        dict[x].append(y)
        dict[y].append(x)
    
    # print(dict)
    def bfs(start,v1,v2):
        de = deque([start])
        visited = [False] * (n+1)
        visited[start] = True
        count = 1
        while de:
            curr = de.popleft()
            for neigh in dict[curr]:
                if (curr == v1 and neigh == v2) or (curr == v2 and neigh == v1):
                    continue
                    
                if not visited[neigh]:
                    visited[neigh] = True
                    de.append(neigh)
                    count += 1
        return count
        
    for v1 ,v2 in wires:
        route1 = bfs(v1,v1,v2)
        route2 = n - route1
        
        tmp = abs(route1-route2)
        answer = min(answer, tmp)
        
    
    
    return answer