import sys
input = sys.stdin.readline

for k in range(1, int(input().strip()) + 1):
    C, N = map(int, input().split())
    M = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # total_pop = sum(M)
    for b in B:
        M[b - 1] -= 1

    if k > 1:
        print()
    print(f'Data Set {k}:')
    print(max(M))