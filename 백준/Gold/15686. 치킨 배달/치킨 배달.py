import sys
from itertools import combinations

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    
    houses = []
    chickens = []
    
    for r in range(N):
        row = list(map(int, input().split()))
        for c in range(N):
            if row[c] == 1:
                houses.append((r, c))
            elif row[c] == 2:
                chickens.append((r, c))

    result = float('inf')

    # 1. 치킨집 중에서 M개를 뽑는 조합 순회
    for selected_chickens in combinations(chickens, M):
        #print(selected_chickens)
        city_chicken_distance = 0
        
        
        for hy, hx in houses:
            temp_min = float('inf')
            for cy, cx in selected_chickens:
                dist = abs(hy - cy) + abs(hx - cx)
                temp_min = min(temp_min, dist) # 가장 가까운 치킨집 선택
            
            city_chicken_distance += temp_min
        
        # 3. 도시의 치킨 거리 중 최솟값 업데이트
        result = min(result, city_chicken_distance)

    print(result)

if __name__ == "__main__":
    main()