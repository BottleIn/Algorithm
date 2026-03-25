import sys

def main():
    input = sys.stdin.readline

    # 1) N
    N = int(input().strip())

    # 2) 단어 N개 (각 줄에 하나)
    words = [input().strip() for _ in range(N)]
    ans = 0
    for word in words:
        stack = []
        for wrd in word:
            if not stack:
                stack.append(wrd)
            elif stack[-1] == wrd:
                stack.pop()
            else:
                stack.append(wrd)

        if not stack:
            ans += 1
    print(ans)
if __name__ == "__main__":
    main()