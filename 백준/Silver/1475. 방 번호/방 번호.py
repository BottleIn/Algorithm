import sys
import math
def main():
    input = sys.stdin.readline

    # 1) 방 번호 N (문자열로 받는 게 편함)
    N = input().strip()
    lst = [0] * 10
    
    for n in N:
        lst[int(n)] += 1
    
    need_num = lst[6] + lst[9]
    lst[6] = math.ceil(need_num / 2)
    lst[9] = 0

    print(max(lst))
if __name__ == "__main__":
    main()