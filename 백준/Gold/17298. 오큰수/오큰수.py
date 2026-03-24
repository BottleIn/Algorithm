import sys

def main():
    input = sys.stdin.readline

    # 1) N
    N = int(input().strip())

    # 2) 수열 A (N개)
    A = list(map(int, input().split()))

    ans = [-1] * N
    stack = []
    for idx, x in enumerate(A):
        #print(stack)
        while stack and stack[-1][1] < x:
            ans[stack[-1][0]] = x
            stack.pop()
    
        stack.append((idx,x))
    for x in ans:
        print(x, end=' ')
if __name__ == "__main__":
    main()