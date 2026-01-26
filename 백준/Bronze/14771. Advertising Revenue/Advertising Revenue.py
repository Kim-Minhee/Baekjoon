import sys
input = sys.stdin.readline

for k in range(1, int(input().strip()) + 1):
    N, V = map(int, input().split())
    ads = [tuple(map(int, input().split())) for _ in range(N)]
    total_fee = 0
    for _ in range(V):
        A1, A2, C = map(int, input().split())
        if ads[A1 - 1][0] == 1 or (ads[A1 - 1][0] == 0 and C == 1):
            total_fee += ads[A1 - 1][1]
        if ads[A2 - 1][0] == 1 or (ads[A2 - 1][0] == 0 and C == 2):
            total_fee += ads[A2 - 1][1]
    if k > 1:
        print()
    print(f'Data Set {k}:')
    print(total_fee)