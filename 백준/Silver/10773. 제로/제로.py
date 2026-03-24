import sys
from collections import deque
def main():
    input = sys.stdin.readline

    # 1) K
    K = int(input().strip())

    # 2) 숫자 K줄
    nums = [int(input().strip()) for _ in range(K)]
    ans = deque()

    for x in nums:
        if x == 0 and ans:
            ans.pop()
        else:
            ans.append(x)
    #print(ans)
    print(sum(ans))


if __name__ == "__main__":
    main()