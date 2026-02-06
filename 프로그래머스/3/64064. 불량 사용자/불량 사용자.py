def solution(user_id, banned_id):
    answer = set()  # 중복된 조합을 자동으로 제거하기 위해 set 사용
    visited_user_id = [False] * len(user_id)
    N = len(banned_id)

    # 두 아이디가 매칭되는지 확인하는 헬퍼 함수
    def is_match(user, banned):
        if len(user) != len(banned):
            return False
        for u, b in zip(user, banned):
            if b != '*' and u != b:
                return False
        return True

    def dfs(n, current_lst):
        # 종료 조건: 모든 불량 아이디에 대해 매칭을 완료했을 때
        if n == N:
            #print(current_lst)
            answer.add(tuple(sorted(current_lst)))
            return

        # n번째 불량 아이디(banned_id[n])와 매칭될 user_id를 찾음
        for i in range(len(user_id)):
            # 1. 아직 사용하지 않은 유저이고
            # 2. 아이디 패턴이 일치한다면
            # print(user_id[i], banned_id[n] )
            if not visited_user_id[i] and is_match(user_id[i], banned_id[n]):
                visited_user_id[i] = True           # 방문 처리
                dfs(n + 1, current_lst + [user_id[i]]) # 다음 단계로 (리스트 합치기)
                visited_user_id[i] = False          # 백트래킹 (원상 복구)

    dfs(0, [])
    
    return len(answer)