import sys

def main():
    input = sys.stdin.readline

    # 1. 입력 받기 및 초기 변수 설정
    s = input().strip()
    stack = []
    is_valid = True  # 올바른 괄호열인지 체크하는 플래그

    for x in s:
        # 2. 여는 괄호('(', '[')는 종류 상관없이 스택에 추가
        if x == "(" or x == "[":
            stack.append(x)
        
        # 3. 닫는 괄호 ')'를 만났을 때
        elif x == ")":
            tmp = 0
            # 3-1. 스택의 top이 숫자라면, '('를 만날 때까지 꺼내서 tmp에 합산
            while stack and isinstance(stack[-1],int):
                tmp += stack.pop()
            
            # 3-2. 스택이 비었거나 짝이 맞지 않는('[') 경우 잘못된 문자열
            if not stack or stack[-1] != '(':
                is_valid = False
                break
            
            # 3-3. '('를 제거하고, ()면 2를, (X)면 2 * X를 스택에 다시 넣음
            stack.pop()
            stack.append(2 if tmp == 0 else tmp*2)

        # 4. 닫는 괄호 ']'를 만났을 때
        elif x == "]":
            tmp = 0
            # 4-1. 스택의 top이 숫자라면, '['를 만날 때까지 꺼내서 tmp에 합산
            while stack and isinstance(stack[-1],int):
                tmp += stack.pop()
            
            # 4-2. 스택이 비었거나 짝이 맞지 않는('(') 경우 잘못된 문자열
            if not stack or stack[-1] != '[':
                is_valid = False
                break
            
            # 4-3. '['를 제거하고, []면 3을, [X]면 3 * X를 스택에 다시 넣음
            stack.pop()
            stack.append(3 if tmp == 0 else tmp*3)

    # 5. 최종 결과 출력
    if not is_valid:
        print(0)
    else:
        answer = 0
        for num in stack:
            if not isinstance(num, int):
                print(0)
                return
            answer += num
        print(answer)
        

if __name__ == "__main__":
    main()