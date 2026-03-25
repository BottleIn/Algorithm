import sys
from collections import deque
def main():
    input = sys.stdin.readline

    # 1) N, M
    N, M = map(int, input().split())

    # 2) 뽑아낼 위치 M개
    targets = deque(map(int, input().split()))

    nums = deque()
    for i in range(1,N+1):
        nums.append(i)
    
    ans = 0

    while targets:
        target_num = targets.popleft()
        
        if nums[0] == target_num:
            nums.popleft()
            continue
        
        left = abs(0 - nums.index(target_num))
        right = abs(len(nums) - nums.index(target_num))

        if left <= right:
            ans += left
            nums.rotate(-left)
        else:
            ans += right
            nums.rotate(right)
        nums.popleft()
    
    print(ans)

if __name__ == "__main__":
    main()