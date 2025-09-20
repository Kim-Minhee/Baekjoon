import sys
input = sys.stdin.readline

for c in range(1, int(input()) + 1):
    N = int(input())
    P = list(map(int, input().split()))
    chk = False
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            d = P[j] - P[i]
            for k in range(j + 1, N):
                if P[k] - P[j] == d:
                    chk = True
                    break
    if chk:
        print(f'Case #{c}: NO')
    else:
        print(f'Case #{c}: YES')