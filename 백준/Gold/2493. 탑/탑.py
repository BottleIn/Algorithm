import sys

def main():
    input = sys.stdin.readline

    # 1) N
    N = int(input().strip())

    # 2) 탑 높이 N개
    heights = list(map(int, input().split()))
    stack = []
    ans = []
    for idx, x in enumerate(heights):
        
        while stack and stack[-1][1] < x:
                stack.pop()
            
        
        if not stack:
             ans.append(0)
            
        elif stack[-1][1] >= x:
            ans.append(stack[-1][0] + 1)

        stack.append((idx,x))
    
    for x in ans:
         print(x, end= " ")
        
if __name__ == "__main__":
    main()