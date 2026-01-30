def solution(n):
    answer = []
    nums = [[0 for _ in range(n)] for _ in range(n)]
    nums[0][0] = 1

    total_num = 0
    for x in range(1, n + 1):
        total_num += x

    case = 1
    x = 0
    y = 0
    need_num = 1

    while need_num < total_num:  # ✅ (1) 종료조건 수정: != -> <
        if case == 1:
            # ✅ (2) 아래로: "갈 수 있을 때까지" 한 칸씩
            while x + 1 < n and nums[x + 1][y] == 0:
                x += 1
                need_num += 1
                nums[x][y] = need_num
            case = 2

        elif case == 2:
            # ✅ (2) 오른쪽: 삼각형 범위 안에서 "갈 수 있을 때까지" 한 칸씩
            while y + 1 < n and nums[x][y + 1] == 0:
                y += 1
                need_num += 1
                nums[x][y] = need_num
            case = 3

        else:  # case == 3
            # ✅ (2) 왼쪽-위 대각선: "갈 수 있을 때까지" 한 칸씩 + 경계 체크
            while x - 1 >= 0 and y - 1 >= 0 and nums[x - 1][y - 1] == 0:
                x -= 1
                y -= 1
                need_num += 1
                nums[x][y] = need_num
            case = 1

    # ✅ (3) 삼각형만 answer로 펼치기 (y <= x)
    for i in range(n):
        for j in range(i + 1):
            answer.append(nums[i][j])

    return answer


