import sys
input = sys.stdin.readline

for t in range(1, int(input().strip()) + 1):
    N = int(input().strip())
    windows = [tuple(map(int, input().split())) for _ in range(N)]

    cross_cnt = 0
    for i, (a1, b1) in enumerate(windows):
        for a2, b2 in windows[i + 1:]:
            if (a1 < a2 and b1 > b2) or (a1 > a2 and b1 < b2):
                cross_cnt += 1
    print(f'Case #{t}: {cross_cnt}')