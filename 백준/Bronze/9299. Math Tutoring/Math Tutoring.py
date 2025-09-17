import sys
input = sys.stdin.readline

for i in range(1, int(input()) + 1):
    F = list(map(int, input().split()))
    r = []
    for n in range(F[0], 0, -1):
        r.append(str(n * F[-(n + 1)]))
    print(f'Case {i}: {F[0] - 1} {" ".join(r)}')