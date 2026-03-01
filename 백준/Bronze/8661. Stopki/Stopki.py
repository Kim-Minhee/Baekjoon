import sys
input = sys.stdin.readline

X, K, A = map(int, input().split())
X %= (K + A)
if X < K:
    print(1)
else:
    print(0)