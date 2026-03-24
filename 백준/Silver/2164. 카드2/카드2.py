import sys
from collections import deque
def main():
    input = sys.stdin.readline

    # 1) N
    N = int(input().strip())

    dq = deque()

    for x in range(1,N+1):
        dq.append(x)
    #print(dq)

    while len(dq) != 1 :
        dq.popleft()
        dq.append(dq.popleft())
    print(dq[-1])
if __name__ == "__main__":
    main()