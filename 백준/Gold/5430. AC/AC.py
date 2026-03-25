import sys
from collections import deque

def main():
    input = sys.stdin.readline
    # 1) 테스트 케이스 T
    try:
        line = input().strip()
        if not line: return # 입력이 없는 경우 종료
        T = int(line)
    except ValueError:
        return

    for _ in range(T):
        # 2) 함수 문자열 p
        command = input().strip()

        # 3) 배열 길이 n
        n = int(input().strip())

        # 4) 배열 문자열 처리 (핵심!)
        raw_arr = input().strip()[1:-1]
        if n == 0:
            nums = deque()
        else:
            nums = deque(raw_arr.split(','))
        
        reverse_flag = False
        is_error = False

        for cmd in command:
            if cmd == "R":
                # 실제로 뒤집지 않고 상태만 기록
                reverse_flag = not reverse_flag
            elif cmd == "D":
                if not nums:
                    print("error")
                    is_error = True
                    break
                
                # 뒤집힌 상태라면 뒤에서 빼고(pop), 아니면 앞에서 뺌(popleft)
                if reverse_flag:
                    nums.pop()
                else:
                    nums.popleft()
        
        # 에러가 발생하지 않은 경우에만 결과 출력
        if not is_error:
            if reverse_flag:
                nums.reverse() # 출력 전 마지막에 한 번만 실제로 뒤집음
            
            # 출력 형식을 [1,2,3] 형태로 맞춤 (공백 없이)
            print("[" + ",".join(nums) + "]")

if __name__ == "__main__":
    main()