from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    road = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    #print(truck_weights[0])
    time = 0
    while truck_weights:
        time += 1
        
        
        
        t = road.popleft()
        weight += t
        
        if truck_weights[0] <= weight:
            tmp = truck_weights.popleft()
            road.append(tmp)
            weight -= tmp
        else:
            road.append(0)
    
    while road:
        time += 1
        road.popleft()
        
        
    return time