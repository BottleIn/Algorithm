import sys

def main():
    input = sys.stdin.readline

    # 1) 초기 문자열
    left= list(sys.stdin.readline().strip())

    # 2) 명령 개수 M
    M = int(input().strip())

    # 3) 명령 M줄
    commands = [input().split() for _ in range(M)]
    # 예: ["L"], ["D"], ["B"], ["P", "x"]

    right = []
    
    for cmd in commands:
        if cmd[0] == "L":
            if left:
                right.append(left.pop())
        
        elif cmd[0] == "D":
            if right:
                left.append(right.pop())
        
        elif cmd[0] == "B":
            if left:
                left.pop()
        
        elif cmd[0] == "P":
            left.append(cmd[1])
    
    print(''.join(left) + ''.join(reversed(right)))


if __name__ == "__main__":
    main()