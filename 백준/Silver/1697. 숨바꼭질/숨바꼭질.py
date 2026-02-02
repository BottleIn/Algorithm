import sys
from collections import deque
sys.setrecursionlimit(10000)
def main():
    input = sys.stdin.readline

    N, K = map(int, input().split())
    # 입력만 받는 코드 (출력 없음)
    d = deque([N])
    nums = [-1 for _ in range(100001)]
    nums[N] = 0
    while d:
        #print(d)
        num = d.popleft()
        if num == K:
            print(nums[num])
            break
        
        if 0<=num+1 <= 100000 and nums[num+1] == -1:
            d.append(num+1)
            nums[num+1] = nums[num] + 1
        if 0 <= num-1 <= 100000 and nums[num-1] == -1:
            d.append(num-1)
            nums[num-1] = nums[num] + 1
        if 0<=num*2 <= 100000 and nums[num*2] == -1:
            d.append(num*2)
            nums[num*2] = nums[num] + 1

        
       

if __name__ == "__main__":
    main()
