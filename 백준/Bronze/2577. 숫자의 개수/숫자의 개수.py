import sys

def main():
    input = sys.stdin.readline

    # 1) A, B, C (각 줄에 하나씩)
    A = int(input().strip())
    B = int(input().strip())
    C = int(input().strip())

    cnt = A * B * C
    #print(cnt)
    ans = [0  for _ in range(10)]
    while cnt > 0:
        tmp  = cnt % 10
        cnt = int(cnt / 10 )
        #print(tmp,cnt)
        ans[tmp] += 1
    
    for x in ans:
        print(x)        
if __name__ == "__main__":
    main()