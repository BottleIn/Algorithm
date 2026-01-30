import sys
from collections import defaultdict
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

    order = [0] * (N + 1)
    cnt = 1

    def dfs(v):
        nonlocal cnt
        order[v] = cnt
        cnt += 1
        for nx in edges[v]:
            if order[nx] == 0:
                dfs(nx)

    dfs(R)

    for i in range(1, N + 1):
        print(order[i])

if __name__ == "__main__":
    main()
