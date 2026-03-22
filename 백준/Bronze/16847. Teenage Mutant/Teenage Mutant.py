import sys
input = sys.stdin.readline

for x in range(1, int(input().strip()) + 1):
    N, K = map(int, input().split())
    MY = input().strip()
    pg = {}
    for _ in range(N):
        G = input().strip()
        for i in range(K):
            temp = pg.get(i, '')
            pg[i] = temp + G[i]

    cnt = 0
    for i in range(K):
        if MY[i] not in pg[i]:
            cnt += 1
    print(f'Data Set {x}:')
    print(f'{cnt}/{K}')
    print()