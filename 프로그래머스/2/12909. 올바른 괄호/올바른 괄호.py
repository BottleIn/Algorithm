def solution(s):
    answer = True
    stack = []
    for str in s:
        # print(str)
        if len(stack) == 0:
            stack.append(str)
            # print(f"비어있어 추가 {stack}")
        else:
            compare_str = stack[-1]
            # print(compare_str)
            if compare_str != '(' or str != ')':
                stack.append(str)
                # print(f"안맞아서 추가 {stack}")
            else: # 닫힌 상황
                stack.pop()
    return not len(stack)



print(solution(")()("))