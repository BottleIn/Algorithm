import sys
from collections import deque, defaultdict
def main():
    input = sys.stdin.readline

    # 1) 뿌요판 12줄, 각 줄 6칸
    board = [list(input().strip()) for _ in range(12)]
    total_chain = 0
    def bfs(y,x,visited,cur_connected):
        dq = deque()
        cur_set = []
        dq.append((y,x))
        visited[y][x] = True
        cur_set.append((y,x))
        while dq:
            cy,cx = dq.popleft()

            for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                ny = cy + dy
                nx = cx + dx

                if 0<= ny < 12 and 0<= nx < 6 and not visited[ny][nx] and board[cy][cx] == board[ny][nx]:
                    dq.append((ny,nx))
                    visited[ny][nx] = True
                    cur_set.append((ny,nx))
        
        # 4개 이상 연결된 경우만 터뜨릴 목록에 추가
        if len(cur_set) >= 4:
            cur_connected.append(cur_set)
    
    while True:
        cur_connected = []
        visited = [[False for _ in range(6)]for _ in range(12)]
        
        for y in range(12):
            for x in range(6):
                if board[y][x] != '.':
                    if not visited[y][x]:
                        bfs(y,x,visited,cur_connected)
        
        #디버깅
        #print(cur_connected)

        # 더이상 연쇄 세트가 없으면 종료
        if not cur_connected:
            break
        
        total_chain += 1
        for group in cur_connected:
            for y, x in group:
                board[y][x] = '.'

        for x in range(6):
            # 아래에서 위로 올라가며 빈칸이 아닌 것만 모음
            temp = deque()
            for y in range(11, -1, -1):
                if board[y][x] != '.':
                    temp.append(board[y][x])
            
            # 다시 아래에서 위로 채우고, 남은 위쪽은 빈칸 처리
            for y in range(11, -1, -1):
                if temp:
                    board[y][x] = temp.popleft()
                else:
                    board[y][x] = '.'
    print(total_chain)

if __name__ == "__main__":
    main()