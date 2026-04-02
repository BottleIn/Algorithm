import sys
from collections import deque

def main():
    input = sys.stdin.readline

    # 1) 톱니바퀴 4개 상태
    gears = [deque(input().strip()) for _ in range(4)]

    # 2) 회전 횟수 K
    K = int(input().strip())

    # 3) 회전 정보 K줄
    rotations = [tuple(map(int, input().split())) for _ in range(K)]

    for k in range(K):
        rotate_num, rotate_dir = rotations[k]
        target_idx = rotate_num - 1  # 0번 인덱스로 보정
        
        # 이번 회차에서 회전할 정보를 담을 리스트
        cur_rotation = [(target_idx, rotate_dir)]
        
        # 오른쪽 방향 조사
        tmp_dir = rotate_dir
        for i in range(target_idx, 3):
            if gears[i][2] != gears[i+1][6]:
                tmp_dir = -tmp_dir
                cur_rotation.append((i+1, tmp_dir))
            else:
                break
        
        # 왼쪽 방향 조사
        tmp_dir = rotate_dir
        for i in range(target_idx, 0, -1):
            if gears[i][6] != gears[i-1][2]:
                tmp_dir = -tmp_dir
                cur_rotation.append((i-1, tmp_dir))
            else:
                break
        
        # 모든 조사가 끝난 후 한꺼번에 회전 (중요!)
        for idx, direction in cur_rotation:
            gears[idx].rotate(direction)

    # 최종 점수 계산 (N극:0, S극:1)
    ans = 0
    for i in range(4):
        if gears[i][0] == '1':
            ans += (2**i)
    print(ans)

if __name__ == "__main__":
    main()