N, X, K = map(int, input().split())
for _ in range(K):
  a, b = map(int, input().split())
  if a==X:
    X = b
  elif b==X:
    X = a
print(X)