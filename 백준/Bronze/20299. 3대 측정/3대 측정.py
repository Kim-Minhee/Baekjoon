import sys

N, K, L = map(int, sys.stdin.readline().split())

vips = []
for _ in range(N):
  X = list(map(int, sys.stdin.readline().split()))
  if sum(X)>=K:
    vip = []
    for x in X:
      if x>=L: vip.append(x)
      else: break
    if len(vip)==3:
      vips += vip

print(len(vips)//3)
print(*vips)