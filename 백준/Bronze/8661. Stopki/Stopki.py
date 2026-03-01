X, K, A = map(int, input().split())
X = X % (K + A)
if X < K:
    print(1)
else:
    print(0)