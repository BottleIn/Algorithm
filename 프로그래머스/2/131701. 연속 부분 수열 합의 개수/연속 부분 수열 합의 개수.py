def solution(elements):
    n = len(elements)
    # 원형 수열 처리를 위해 리스트를 2배로 늘림 (예: [7,9,1] -> [7,9,1,7,9,1])
    extended_elements = elements * 2
    unique_sums = set()

    # i: 시작 위치
    for i in range(n):
        temp_sum = 0
        # j: 시작 위치부터 길이 n까지 연속해서 더해감
        for j in range(i, i + n):
            temp_sum += extended_elements[j]
            unique_sums.add(temp_sum)
            
    return len(unique_sums)