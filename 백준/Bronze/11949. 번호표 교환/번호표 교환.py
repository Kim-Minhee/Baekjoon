import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [0] + [int(input().strip()) for _ in range(N)]

for i in range(1, M + 1):
    for j in range(1, N):
        if A[j] % i > A[j + 1] % i:
            A[j], A[j + 1] = A[j + 1], A[j]
for a in A[1:]:
    print(a)