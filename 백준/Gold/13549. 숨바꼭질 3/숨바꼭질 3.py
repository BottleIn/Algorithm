import sys
from collections import deque

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())

    if N == K:
        print(0)
        return

    MAX = 100001
    dist = [-1] * MAX
    dist[N] = 0
    dq = deque([N])
    
    while dq:
        x = dq.popleft()
        
        if x == K:
            print(dist[x])
            return
        
        
        nx = 2 * x
        if 0 <= nx < MAX and dist[nx] == -1:
            dist[nx] = dist[x]
            dq.appendleft(nx)
            
        
        for nx in (x - 1, x + 1):
            if 0 <= nx < MAX and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                dq.append(nx)

if __name__ == "__main__":
    main()