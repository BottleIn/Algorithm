'''
1. 테스트 케이스 한개 생각못해서 잘못짬
'''

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)   # 다리 칸(시간)을 그대로 큐로 표현
    current_weight = 0
    trucks = deque(truck_weights)

    while trucks or current_weight > 0: # 트럭이 아직 있음 or 다리에 트럭이 아직 놓아져 있음
        time += 1

        # 1초 경과: 맨 앞 칸이 빠지면서(=다리 통과) 무게도 빠짐
        left = bridge.popleft()
        current_weight -= left

        # 다음 트럭을 올릴 수 있으면 올리고, 아니면 0(빈 칸) 넣기
        if trucks and current_weight + trucks[0] <= weight:
            t = trucks.popleft()
            bridge.append(t)
            current_weight += t
        else:
            bridge.append(0)

    return time
