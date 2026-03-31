import sys
from collections import defaultdict
def main():
    input = sys.stdin.readline

    # 1) N, M
    N, M = map(int, input().split())

    # 2) 수 N개
    nums = list(map(int, input().split()))
    nums.sort()
    #print(nums)
    used_num = defaultdict(bool)
    #print(used_num)
    ans = []
    def backtracking(depth):
        if depth == M :
            if tuple(ans) not in used_num:
                used_num[tuple(ans)] = True
                print(*ans)
            return
        
        for i in nums:
            ans.append(i)
            backtracking(depth+1)
            ans.pop()


    backtracking(0)

if __name__ == "__main__":
    main()