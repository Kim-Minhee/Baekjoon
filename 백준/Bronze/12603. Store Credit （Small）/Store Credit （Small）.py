import sys
input = sys.stdin.readline

for n in range(1, int(input().strip()) + 1):
    C = int(input().strip())
    I = int(input().strip())
    prices = list(map(int, input().split()))
    for a in range(I - 1):
        diff = C - prices[a]
        if diff in prices[a + 1:]:
            b = prices[a + 1:].index(diff) + a + 1
            print(f'Case #{n}: {a + 1} {b + 1}')
            break