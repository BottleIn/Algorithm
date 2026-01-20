def solution(a, b, n):
    answer = 0
    # 갖고 있는 병수 (n) > 바꿀 수 있는 병 (a) 까지
    # 받는 병 (b)
    
    while n >= a:
        x,y = divmod(n,a) # 몫 x , 나머지 y
        answer += x * b
        n = n - a * x + x * b
        print(f"{n}, x: {x}, y: {y}")
    
    
    return answer