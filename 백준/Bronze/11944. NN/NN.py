import sys
input = sys.stdin.readline

N, M = map(int, input().split())
l = len(str(N))
if l * N <= M:
    print(str(N) * N)
else:
    n = str(N) * (M // l + 1)
    print(n[:M])