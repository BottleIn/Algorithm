import sys

def main():
    input = sys.stdin.readline

    # 1) N, M
    N, M = map(int, input().split())

    # 2) 수 N개
    nums = sorted(list(map(int, input().split())))

    ans = []
    def back(start,depth):
        if depth == M:
            print(*(ans))
            return
        prev = -1
        for i in range(start,N):
            cur = nums[i]

            if prev == cur:
                continue
            ans.append(cur)
            prev = cur
            back(i, depth + 1)
            ans.pop()

    back(0,0)

if __name__ == "__main__":
    main()