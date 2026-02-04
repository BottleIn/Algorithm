import sys
input = sys.stdin.readline

# N: 계란의 수 (1 <= N <= 8)
N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]
# eggs[i][0] = 내구도(S), eggs[i][1] = 무게(W)

#print(eggs)
max_broken = 0

def solve(curr_index):
    global max_broken
    
    # [종료 조건] 가장 오른쪽 계란(마지막)까지 과정을 마쳤을 때
    if curr_index == N:
        count = 0
        for i in range(N):
            if eggs[i][0] <= 0: # 내구도가 0 이하인 계란 카운트
                count += 1
        max_broken = max(max_broken, count)
        return

    # [예외 처리 1] 현재 손에 든 계란이 이미 깨져있는 경우
    # 아무것도 치지 않고 다음 계란으로 넘어감
    if eggs[curr_index][0] <= 0:
        solve(curr_index + 1)
        return

    # [로직 수행] 현재 계란으로 다른 계란 깨보기
    hit_any = False # 실제로 계란을 쳤는지 확인하는 플래그
    
    for target_index in range(N):
        # 자기 자신이거나, 이미 깨진 계란은 칠 수 없음
        if target_index == curr_index or eggs[target_index][0] <= 0:
            continue
        
        hit_any = True
        
        # 1. 계란 치기 (내구도 감소)
        eggs[curr_index][0] -= eggs[target_index][1]
        eggs[target_index][0] -= eggs[curr_index][1]
        
        # 2. 다음 단계로 재귀 호출
        solve(curr_index + 1)
        
        # 3. 원상 복구 (백트래킹 핵심) - 다른 경우의 수를 위해 내구도 돌려놓기
        eggs[curr_index][0] += eggs[target_index][1]
        eggs[target_index][0] += eggs[curr_index][1]

    # [예외 처리 2] 칠 수 있는 계란이 하나도 없는 경우
    # (예: 나 빼고 다른 계란이 다 깨져있음) -> 치지 않고 다음 순서로 넘어감
    if not hit_any:
        solve(curr_index + 1)

# 0번 계란부터 시작
solve(0)

print(max_broken)