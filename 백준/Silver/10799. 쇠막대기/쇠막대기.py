import sys

def main():
    input = sys.stdin.readline

    s = input().strip()  # 괄호 문자열 한 줄
    # 입력만 받는 코드 (출력 없음)
    dp = []
    ans = 0
    cur_idx = 0
    for idx,w in enumerate(s):
        # if len(dp) == 0:
        #     dp.append(w)
        if w=='(':
            cur_idx = idx
            dp.append(w)
        elif w == ')':
            if idx - cur_idx == 1: # 레이저
                dp.pop()
                ans += (1*len(dp))
            else:
                dp.pop()
                ans += 1
        #print(dp, ans)
    print(ans)    
            


if __name__ == "__main__":
    main()
