import sys
from collections import defaultdict,deque
sys.setrecursionlimit(10**7)

def main():
    input = sys.stdin.readline
    N, M, R = map(int, input().split())

    edges = defaultdict(list)
    for _ in range(M):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)

    for k in edges:
        edges[k].sort()  # 오름차순
    #print(edges)
    order = [0] * (N + 1)
    cnt = 1
    
    def bfs(start):
        d = deque()
        nonlocal cnt
        order[start] = cnt
        d.append(start)

        while d:
            cur = d.popleft()
            for x in edges[cur]:
                if order[x] == 0:
                    cnt += 1
                    order[x] = cnt
                    d.append(x)


    bfs(R)


    for i in range(1, N + 1):
        print(order[i])

    
if __name__ == "__main__":
    main()
