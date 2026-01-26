def solution(dirs):
    # 길을 저장할 집합 (중복 자동 제거)
    visited_paths = set()
    
    # 현재 위치
    x, y = 5, 5
    
    # 방향 매핑
    move = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    
    for way in dirs:
        dx, dy = move[way]
        nx, ny = x + dx, y + dy
        
        # 범위를 벗어나면 무시
        if not (0 <= nx <= 10 and 0 <= ny <= 10):
            continue
            
        # (출발점, 도착점)과 (도착점, 출발점)을 동일한 길로 취급하여 추가
        # 튜플로 묶어서 세트에 넣으면 중복이 알아서 제거됨
        path = tuple(sorted([(x, y), (nx, ny)]))
        visited_paths.add(path)
        
        # 위치 이동
        x, y = nx, ny
        
    return len(visited_paths)