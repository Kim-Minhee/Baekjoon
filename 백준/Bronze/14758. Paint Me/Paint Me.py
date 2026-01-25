import sys, math
input = sys.stdin.readline

while True:
    N, W, L, H, A, M = map(int, input().split())
    if N + W + L + H + A + M == 0:
        break
    needed_paint = (L + W) * H * 2 + W * L
    for _ in range(M):
        DW, DH = map(int, input().split())
        needed_paint -= DW * DH
    total_needed_paint = N * needed_paint
    r = math.ceil(total_needed_paint / A)
    print(r)