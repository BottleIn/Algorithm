def solution(n, stations, w):
    answer = 0
    range_width = 2 * w + 1  # 기지국당 총 커버 개수
    current = 1            # 아직 전파가 닿지 않은 아파트 중, 가장 왼쪽(처음)에 있는 아파트의 번호 

    for station in stations:
        # 이번 기지국의 전파가 닿기 시작하는 왼쪽 끝 지점
        start_coverage = station - w
        
        # 현재 위치(current)가 전파 닿는 곳보다 전 -> 빈 공간(Gap) 존재
        if current < start_coverage:
            gap_length = start_coverage - current
            
            
            # 빈 공간을 채우기 위해 필요한 기지국 수 계산 (올림 나눗셈)
            # 식: (빈길이 + 커버너비 - 1) // 커버너비
            count = gap_length // range_width + (1 if gap_length % range_width else 0)
            answer += count
        
        # 현재 위치를 이번 기지국의 전파가 끝나는 곳 (오른쪽)
        current = station + w + 1

    # 모든 기지국을 다 확인했는데, 아직 아파트가 남아있는 경우 (오른쪽 끝 잔여 구간)
    if current <= n:
        gap_length = n - current + 1
        count = gap_length // range_width + (1 if gap_length % range_width else 0)
        answer += count

    return answer