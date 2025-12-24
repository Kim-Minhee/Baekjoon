import sys
input = sys.stdin.readline

prices = [float(input().strip()) for _ in range(int(input().strip()))]
prices.sort()
print(f'{prices[1]:.2f}')