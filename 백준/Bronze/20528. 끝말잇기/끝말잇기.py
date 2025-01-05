N, P = int(input()), list(input().split())
f, r = P[0][0], 1
for p in P[1:]:
  if p[0]!=f:
    r = 0
    break
print(r)