from collections import defaultdict,deque


def solution(n, computers):
    answer = 0
    visited = [False] * n
    # print(visited)
    q = deque()
    def bfs(start):

        nonlocal visited,answer
        if visited[start] == True:
            return
        
        q.append(start)

        while q:
            cur = q.popleft()
            visited[cur] = True
            for idx, val in enumerate(computers[cur]):
                if visited[idx] == False:
                    if idx != start and val == 1:
                        #print(idx, start)
                        q.append(idx)
                        #print(q)
        answer += 1
                    
    for x in range(n):
        bfs(x)
    return answer

# print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))