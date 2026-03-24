import sys

def main():
    input = sys.stdin.readline

    # 1) 문자열 S
    S = input().strip()

    alp  = [0 for _ in range(26)]
    #print(ord("a"))

    for wrd in S:
        idx = ord(wrd) - 97
        alp[idx] += 1

    for x in alp:
        print(x, end = ' ')
if __name__ == "__main__":
    main()