import sys
from collections import deque

def main():
    input = sys.stdin.readline
    M, N, H = map(int, input().split())  # M=x, N=y, H=z

    box = []
    q = deque()

    for z in range(H):
        layer = []
        for y in range(N):
            row = list(map(int, input().split()))
            layer.append(row)
            for x in range(M):
                if row[x] == 1:
                    q.append((z, y, x))
        box.append(layer)

    # 6방향: (z,y,x)
    dz = (1, -1, 0, 0, 0, 0)
    dy = (0, 0, 1, -1, 0, 0)
    dx = (0, 0, 0, 0, 1, -1)

    while q:
        z, y, x = q.popleft()
        for k in range(6):
            nz, ny, nx = z + dz[k], y + dy[k], x + dx[k]
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
                if box[nz][ny][nx] == 0:
                    box[nz][ny][nx] = box[z][y][x] + 1
                    q.append((nz, ny, nx))

    max_day = 1
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if box[z][y][x] == 0:
                    print(-1)
                    return
                if box[z][y][x] > max_day:
                    max_day = box[z][y][x]

    print(max_day - 1)

if __name__ == "__main__":
    main()
