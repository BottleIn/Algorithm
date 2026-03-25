import sys

def main():
    input = sys.stdin.readline

    # 1) 괄호 문자열
    s = input().strip()
    ans = 0
    stack = []
    #total_steal = 0
    for idx, wrd in enumerate(s):
        if wrd == '(':
            stack.append(wrd)
        
        # ) 가 들어올 경우
        else:
            stack.pop()
            if s[idx-1] == '(': # 레이저  
               ans += len(stack) # 지금까지의 철 개수 : '('
            else: # 철 길이가 끝남
                ans += 1
            
        #print(stack,ans)
    print(ans)

if __name__ == "__main__":
    main()