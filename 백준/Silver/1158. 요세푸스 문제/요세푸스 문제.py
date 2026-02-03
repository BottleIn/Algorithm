import sys
from collections import deque
def main():
    input = sys.stdin.readline

    N, K = map(int, input().split())
    # 입력만 받는 코드 (출력 없음)
    dp = deque()
    for x in range(1,N+1):
        dp.append(x)
    ans = []
    tp = 0
    while dp:
        tp += 1
        if tp == K:
            ans.append(dp.popleft())
            tp = 0
            continue
        dp.append(dp.popleft())
    result = f"<{', '.join(map(str, ans))}>"
    print(result)
if __name__ == "__main__":
    main()
