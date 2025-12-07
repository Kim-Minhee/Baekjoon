import sys

INPUT_DATA = sys.stdin.read().split()
data = iter(INPUT_DATA)

for t in range(1, int(next(data)) + 1):
    n = int(next(data))
    windows = []
    for _ in range(n):
        a = int(next(data))
        b = int(next(data))
        windows.append((a, b))

    cross_cnt = 0
    for i, (a1, b1) in enumerate(windows):
        for a2, b2 in windows[i + 1:]:
            if (a1 < a2 and b1 > b2) or (a1 > a2 and b1 < b2):
                cross_cnt += 1
    print(f'Case #{t}: {cross_cnt}')