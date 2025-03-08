import math

R, K, M = map(int, input().split())

for i in range(M//K):
  R *= (1/2)
  R = math.trunc(R)
  if R<1:
    R = 0
    break

print(R)