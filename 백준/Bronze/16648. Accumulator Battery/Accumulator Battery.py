import sys
input = sys.stdin.readline

T, P = map(int, input().split())
if P >= 20:
    v = (100 - P) / T
    t = (P + 20) / v
else:
    v = (120 - 2 * P) / T
    t = 2 * P / v
print(t)