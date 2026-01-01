import sys
input = sys.stdin.readline

M, N, K = map(int, input().split())
signs = [input().strip() for _ in range(M)]
for sign in signs:
    for _ in range(K):
        r = [s * K for s in sign]
        print(''.join(r))