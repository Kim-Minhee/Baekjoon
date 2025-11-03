# GPT 5
import sys
input = sys.stdin.readline

while True:
    C, W, L, P = map(int, input().split())
    if C == W == L == P == 0:
        break
    print(C ** (W * L * P))