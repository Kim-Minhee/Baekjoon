import sys
input = sys.stdin.readline

while True:
    N, M = map(int, input().split())
    if N == M == 0:
        break
    A = list(map(int, input().split()))
    max_price = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            price = A[i] + A[j]
            if price <= M and price > max_price:
                max_price = price
    print(max_price if max_price != 0 else 'NONE')