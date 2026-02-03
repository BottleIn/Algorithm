import sys

def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    # 입력만 받는 코드 (출력 없음)

    ans = []
    visited = [False] * (N+1)
    visited[0] = True 
    #print(visited)
    
    def backtracking(depth):
        if depth == M:
            for x in ans:
                print(x,end=' ')
            print()
            return
        
        for i in range(1, N+1):
            if not visited[i]:
                ans.append(i)
                visited[i] = True

                backtracking(depth+1)

                ans.pop()
                visited[i] = False
    backtracking(0)


if __name__ == "__main__":
    main()
