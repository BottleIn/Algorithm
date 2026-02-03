import sys
input = sys.stdin.readline

def z_recursive(N, r, c):
    # [Base Case] N=0이면 더 이상 쪼갤 수 없으므로 0 반환
    if N == 0:
        return 0
    
    # 한 변의 절반 길이 (2^(N-1))
    half = 2 ** (N - 1)
    # 한 사분면의 칸 수 (half * half)
    quad_size = half * half
    
    # 1사분면 (좌상단)
    if r < half and c < half:
        return z_recursive(N - 1, r, c)
        
    # 2사분면 (우상단)
    elif r < half and c >= half:
        # 1사분면 크기만큼 더하고, 좌표를 왼쪽으로 당김
        return quad_size + z_recursive(N - 1, r, c - half)
        
    # 3사분면 (좌하단)
    elif r >= half and c < half:
        # 1, 2사분면 크기만큼 더하고, 좌표를 위로 당김
        return 2 * quad_size + z_recursive(N - 1, r - half, c)
        
    # 4사분면 (우하단)
    else:
        # 1, 2, 3사분면 크기만큼 더하고, 좌표를 대각선 위로 당김
        return 3 * quad_size + z_recursive(N - 1, r - half, c - half)

# 입력 및 실행
N, r, c = map(int, input().split())
print(z_recursive(N, r, c))