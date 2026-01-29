import sys

def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    queries = [tuple(map(int, input().split())) for _ in range(M)]

    #print(N, M)
    dp = []
    dp.append(numbers[0])
    for idx in range(1,len(numbers)):
        #print(idx)
        dp.append(dp[idx-1] + numbers[idx])

    dp.insert(0,0)
    #print(dp)
    for start, end in queries:
        print(dp[end]-dp[start-1])


    #print(queries)

if __name__ == "__main__":
    main()
