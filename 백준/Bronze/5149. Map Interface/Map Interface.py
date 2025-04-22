# GPT
K = int(input())
for k in range(1, K + 1):
    N, M = map(int, input().split())

    STATION = [tuple(map(int, input().split())) for _ in range(N)]

    VISIT = list(map(int, input().split()))
    VISIT_COORDS = [STATION[v - 1] for v in VISIT]

    xs = [x for x, y in VISIT_COORDS]
    ys = [y for x, y in VISIT_COORDS]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    cnt = sum(min_x <= x <= max_x and min_y <= y <= max_y for x, y in STATION)

    if k != 1:
        print()
    print(f"Data Set {k}:")
    print(cnt)