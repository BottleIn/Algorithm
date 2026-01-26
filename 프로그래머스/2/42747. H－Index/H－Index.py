def solution(citations):
    citations.sort()
    tmp = len(citations)
    candi = tmp // 2 if tmp % 2 == 0 else tmp // 2 + 1

    while True:
        # candi 이상인 논문 수 세기
        max_nums = 0
        for x in citations[::-1]:
            if x >= candi:
                max_nums += 1
            else:
                break

        # ✅ H-index 조건: candi편 이상이 candi번 이상 인용
        if max_nums >= candi:
            # ✅ "최댓값"인지 확인 (candi+1이 불가능하면 candi가 정답)
            next_candi = candi + 1
            next_max = 0
            for x in citations[::-1]:
                if x >= next_candi:
                    next_max += 1
                else:
                    break

            if next_max < next_candi:
                return candi

            # 더 큰 값도 가능하면 계속 올려보기
            candi += 1
        else:
            # 너무 큰 값이면 줄이기
            candi -= 1

            # 안전장치: candi가 0 밑으로 내려가면 답은 0
            if candi < 0:
                return 0
