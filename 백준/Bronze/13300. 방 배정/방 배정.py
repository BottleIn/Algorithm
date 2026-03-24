import sys
import math
from collections import defaultdict
def main():
    input = sys.stdin.readline

    # 1) N, K
    N, K = map(int, input().split())

    # 2) 학생 정보 N줄: S, Y
    students = [tuple(map(int, input().split())) for _ in range(N)]

    # TODO: 로직 작성
    # print(N, K)
    lst = [ [0 for _  in range(3)] for _ in range(7)]
    
    for y,x in students:
        lst[x][y] += 1
    answer = 0 
    for y in range(7):
        for x in range(3):
            answer += math.ceil(lst[y][x]/K)
    print(answer)
if __name__ == "__main__":
    main()