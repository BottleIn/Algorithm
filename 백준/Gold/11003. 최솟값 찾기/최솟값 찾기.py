import sys
from collections import deque

def solve():
    # 입력 받기
    n, l = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    
    dq = deque()
    result = []
    
    # i : 인덱스
    for i in range(n):
        # 1. 덱의 뒤쪽에서 현재 값보다 큰 값들은 모두 제거
        while dq and a[dq[-1]] > a[i]:
            dq.pop()
          
        # 2. 현재 인덱스 추가
        dq.append(i)
        
        # 3. 윈도우 범위를 벗어난 인덱스(i - L + 1 이전)는 앞에서 제거
        if dq[0] <= i - l:
            dq.popleft()
            
        # 4. 덱의 맨 앞이 현재 구간의 최솟값
        result.append(a[dq[0]])
    
    # 결과 출력
    print(*(result))

if __name__ == "__main__":
    solve()