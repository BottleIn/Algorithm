import sys
from collections import deque
def solution(n, w, l, trucks):
    answer = 0

    # n: 트럭 수
    # w: 다리 길이
    # l: 다리의 최대 하중
    # trucks: 각 트럭의 무게 리스트

    dq = deque()
    for _ in range(w):
        dq.append(0)
    #print(dq)
    
    time = 0
    while trucks:
        
        
        l += dq.popleft()
        if trucks[0] <= l:
            cur_truck_weight = trucks.popleft()
        else:
            cur_truck_weight = 0
        
        dq.append(cur_truck_weight)
        l -= cur_truck_weight
        
        time += 1
        #print(dq)

    while sum(dq) != 0:
        time += 1
        dq.popleft()

    return time


if __name__ == "__main__":
    input = sys.stdin.readline

    n, w, l = map(int, input().split())
    trucks = deque(map(int, input().split()))

    print(solution(n, w, l, trucks))