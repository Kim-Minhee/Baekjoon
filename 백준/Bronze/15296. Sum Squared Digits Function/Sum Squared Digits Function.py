import sys, math
input = sys.stdin.readline

for _ in range(int(input().strip())):
    K, B, N = map(int, input().split())
    ssd = 0
    max_degree = int(math.log(N, B))
    for degree in range(max_degree, -1, -1):
        a, mod = divmod(N, B ** degree)
        ssd += a ** 2
        N = mod
    print(K, ssd)