import sys
input = sys.stdin.readline

def solve():
    K, P, X = map(int, input().split())
    m = 1
    min_price = X * m + K / m * P
    while True:
        m += 1
        price = X * m + K / m * P
        if price > min_price:
            print(f'{min_price:.3f}')
            break
        min_price = price

if __name__ == "__main__":
    solve()