import sys, math
input = sys.stdin.readline

for k in range(int(input().strip())):
    N, S, P = map(int, input().split())
    xi, yi = int(), int()
    total_len = 0
    for i in range(N + 1):
        X, Y = map(int, input().split())
        if i != 0:
            total_len += abs(xi - X) + abs(yi - Y)
        xi = X
        yi = Y
    r = math.ceil(total_len * S / P)
    if k != 0:
        print()
    print(f'Data Set {k + 1}:')
    print(r)