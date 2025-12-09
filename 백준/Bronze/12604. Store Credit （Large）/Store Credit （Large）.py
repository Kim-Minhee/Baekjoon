import sys
input = sys.stdin.readline

for n in range(1, int(input().strip()) + 1):
    C = int(input().strip())
    I = int(input().strip())
    prices = list(map(int, input().split()))

    seen = {}
    for idx, price in enumerate(prices, start = 1):
        need = C - price
        if need in seen:
            print(f'Case #{n}: {seen[need]} {idx}')
            break
        seen[price] = idx