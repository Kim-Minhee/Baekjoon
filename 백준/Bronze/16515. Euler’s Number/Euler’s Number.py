import sys
input = sys.stdin.readline

N = int(input().strip())
if N == 0:
    print(1)
else:
    e = 1
    f = 1
    for i in range(1, N + 1):
        f *= i
        e += 1 / f
    print(e)