import sys
from collections import deque

def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())

    ladders = {}
    for _ in range(N):
        a, b = map(int, input().split())
        ladders[a] = b
    
    snakes = {}
    for _ in range(M):
        a, b = map(int, input().split())
        snakes[a] = b

    turn = [0] * 101
    d = deque([1])
    turn[1] = 0  # 시작점은 0회 (문제에 따라 1이나 0으로 초기화 주의, 여기서는 횟수만 세므로 무관하지만 보통 0 시작)

    while d:
        cur = d.popleft()
        
        if cur == 100:
            print(turn[100])
            break
        
        for i in range(1, 7):
            nx = cur + i
            
            if nx <= 100:
                
                if nx in ladders:
                    nx = ladders[nx]
                elif nx in snakes:
                    nx = snakes[nx]

                if turn[nx] == 0:
                    turn[nx] = turn[cur] + 1
                    d.append(nx)

if __name__ == "__main__":
    main()