import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    
    # 건물 높이들을 하나씩 입력받으며 처리
    stack = []
    ans = 0
    
    for _ in range(N):
        height = int(input())
        # 1. stack이 존재하며 나보다 작거나같은 stack애들은 제거
        while stack and stack[-1] <= height:
            stack.pop()
        
        # 2. 남아 있는 왼쪽애들은 새로운 건물이 들어왔을때 볼 수 있는 건물들
        ans += len(stack)

        stack.append(height)
        
    print(ans)

if __name__ == "__main__":
    solve()