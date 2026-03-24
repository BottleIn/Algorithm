import sys
from collections import deque
def main():
    input = sys.stdin.readline

    # 1) N, K
    N, K = map(int, input().split())
    dq = deque(range(1, N + 1))
    #print(nums)
    ans = []
    while dq:
        dq.rotate(-K)
        #print(dq)
        ans.append(dq.pop())
    
    result = f"<{', '.join(map(str, ans))}>"
    print(result)

if __name__ == "__main__":
    main()