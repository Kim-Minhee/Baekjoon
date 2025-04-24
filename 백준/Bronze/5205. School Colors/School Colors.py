# GPT
K = int(input())
for k in range(1, K + 1):
    N = int(input())
    RGB = [tuple(map(int, input().split())) for _ in range(N)]

    max_dist = -1
    results = []

    for i in range(N - 1):
        for j in range(i + 1, N):
            dist = (RGB[i][0] - RGB[j][0]) ** 2 + (RGB[i][1] - RGB[j][1]) ** 2 + (RGB[i][2] - RGB[j][2]) ** 2
            if dist > max_dist:
                max_dist = dist
                results = [(i + 1, j + 1)]
            elif dist == max_dist:
                results.append((i + 1, j + 1))

    print(f'Data Set {k}:')
    for i, j in results:
        print(i, j)