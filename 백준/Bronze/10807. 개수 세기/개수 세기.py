import sys
from collections import Counter
def main():
    input = sys.stdin.readline

    # 1) N
    N = int(input().strip())

    # 2) 정수 N개
    nums = list(map(int, input().split()))

    # 3) 찾을 값 v
    v = int(input().strip())

    a = Counter(nums)
    print(a[v])
if __name__ == "__main__":
    main()