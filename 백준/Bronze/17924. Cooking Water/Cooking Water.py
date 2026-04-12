# GPT 5
import sys
input = sys.stdin.readline

N = int(input().strip())

L = 0
R = 1000

for _ in range(N):
    a, b = map(int, input().split())
    L = max(L, a)
    R = min(R, b)

if L <= R:
    print("gunilla has a point")
else:
    print("edward is right")