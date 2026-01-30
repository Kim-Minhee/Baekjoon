import sys
input = sys.stdin.readline

for t in range(1, int(input().strip()) + 1):
    D, N = map(int, input().split())

    max_time = 0
    for _ in range(N):
        K, S = map(int, input().split())
        time = (D - K) / S
        if time > max_time:
            max_time = time
    speed = D / max_time
    print(f'Case #{t}: {speed:.6f}')