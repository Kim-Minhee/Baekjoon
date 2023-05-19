import math

rh, rv, sh, sv = map(int, input().split())
p = list()
n = int(input())
for i in range(n):
  rhi, rvi, shi, svi, pi = map(int, input().split())
  h1 = max(math.ceil(rh/rhi), math.ceil(sh/shi))
  v1 = max(math.ceil(rv/rvi), math.ceil(sv/svi))
  h2 = max(math.ceil(rh/rvi), math.ceil(sh/svi))
  v2 = max(math.ceil(rv/rhi), math.ceil(sv/shi))
  p.append(min(pi*h1*v1, pi*h2*v2))
print(min(p))