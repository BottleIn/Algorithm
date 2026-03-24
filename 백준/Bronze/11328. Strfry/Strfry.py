import sys
from collections import Counter

def main():
    input = sys.stdin.readline

    # 1) N
    N = int(input().strip())

    # 2) 테스트 케이스 N개: 각 줄에 두 문자열
    pairs = [tuple(input().split()) for _ in range(N)]

    for a, b in pairs:
        if Counter(a) == Counter(b):
            print("Possible")
        else:
            print("Impossible")

if __name__ == "__main__":
    main()