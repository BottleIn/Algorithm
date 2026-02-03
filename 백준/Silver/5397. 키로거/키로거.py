import sys

def main():
    input = sys.stdin.readline

    T = int(input().strip())
    cases = []
    for _ in range(T):
        s = input().rstrip('\n')   # 한 줄에 주어지는 키 입력 문자열
        cases.append(s)

    # 입력만 받는 코드 (출력 없음)
    # print(T)
    #print(cases)
    for word in cases:
        left_words = []
        right_words = []

        for w in word:
            if w == '<':
                if left_words:
                    right_words.append(left_words.pop())
            elif w == '>':
                if right_words:
                    left_words.append(right_words.pop())
            elif w == '-':
                if left_words:
                    left_words.pop()
            else: left_words.append(w)
        print("".join(left_words)+ "".join(reversed(right_words)))
if __name__ == "__main__":
    main()
