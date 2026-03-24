import sys
from collections import defaultdict
def main():
    input = sys.stdin.readline

    # 1) 단어 A, B (각 줄에 하나씩)
    A = input().strip()
    B = input().strip()

    # TODO: 로직 작성
    # print(A, B)
    count_a = [0] * 26
    count_b = [0] * 26

    for a in A:
        count_a[ord(a)-ord('a')] += 1
    for b in B:
        count_b[ord(b)-ord('a')] += 1
    
    result = 0
    for i in range(26):
        result += abs(count_a[i]-count_b[i])
    print(result)
if __name__ == "__main__":
    main()