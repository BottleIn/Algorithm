import sys

for line in sys.stdin:

    data = line.split()
    if not data: # 빈 줄이 들어오는 경우 예외 처리
        continue
    
    s, t = data
    
    s_len = len(s)
    index = 0
    
    # 작성하셨던 로직 그대로 사용
    for x in t:
        if index == s_len:
            break
        if s[index] == x:
            index += 1
            
    if index == s_len:
        print("Yes")
    else:
        print("No")