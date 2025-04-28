# GPT
K = int(input())
for k in range(1, K+1):
    N, M, T1 = map(int, input().split())

    d = [0]*N
    for _ in range(M):
        I, T2, D = input().split()
        I = int(I)
        T2 = int(T2)
        D = float(D)
        if 0 <= T1 - T2 < 1000:
            d[I-1] += D

    v = [input() for _ in range(N)]

    y, n = 0, 0
    for i, vote in enumerate(v):
        if vote == 'N':
            n += 1 / (1 + (d[i] / 10000))
        else:
            y += 1

    if k != 1:
        print()
    print(f'Data Set {k}:')
    print(f'{y:.2f} {n:.2f}')