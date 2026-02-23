import heapq

def solution(book_time):
    
    def to_min(t):
        h, m = map(int, t.split(":"))
        return h * 60 + m

    times = []
    for s, e in book_time:
        start = to_min(s)
        end = to_min(e) + 10  # 청소 10분
        times.append((start, end))

    # 시작 시간 기준 정렬
    times.sort()

    heap = []  # 사용 중인 방들의 "청소 끝나는 시간" (min-heap)
    max_rooms = 0

    for start, end in times:
        # 가장 빨리 비는 방이 start 이전(또는 같은 시각)에 비면 재사용
        if heap and heap[0] <= start:
            heapq.heappop(heap)
            
        heapq.heappush(heap, end)
        max_rooms = max(max_rooms, len(heap))

    return max_rooms