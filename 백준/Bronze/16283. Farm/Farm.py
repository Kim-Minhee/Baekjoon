import sys
input = sys.stdin.readline

A, B, N, W = map(int, input().split())

r = []
for x in range(1, N):
    y = N - x
    if A * x + B * y == W:
        r.append([x, y])

if len(r) == 1:
    print(*r[0])
else:
    print(-1)