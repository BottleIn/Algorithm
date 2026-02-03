import sys

def main():
    input = sys.stdin.readline

    lines = []
    while True:
        line = input().rstrip()
        if not line:          # EOF
            break
        line = line.rstrip('\n')
        if line == '.':       # 종료 조건
            break
        lines.append(line)

    # 입력만 받는 코드 (출력 없음)
    #print(lines)

    for line in lines:
        dp = []
        dp2= []
        for wrd in line:
            if wrd == '[' or wrd == '(':
                dp.append(wrd)
            elif wrd ==']':
            
                if len(dp) != 0 and dp[-1] == '[':
                    dp.pop()
                else: dp.append(wrd)
            elif wrd == ')':
                if len(dp) != 0 and dp[-1] == '(':
                    dp.pop()
                else: dp.append(wrd)
            else:
                dp2.append(wrd)

        
        if len(dp) == 0 and len(dp2) != 0 and dp2[-1] == '.':
            print("yes")
        else: print("no")
    
if __name__ == "__main__":
    main()
