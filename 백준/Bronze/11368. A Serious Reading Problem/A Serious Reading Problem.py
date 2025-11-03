import sys
input = sys.stdin.readline

while True:
    DATA = input().strip()
    if DATA == '0 0 0 0':
        break
    C, W, L, P = map(int, DATA.split())
    print(C ** (W * L * P))