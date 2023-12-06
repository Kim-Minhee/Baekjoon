k, n = int(input()), int(input())
b = 210
for _ in range(n):
  t, z = map(str, input().split())
  if b-int(t)<=0:
    r = k
  else:
    b -= int(t)
    if z=='T':
      k += 1
      if k==9:
        k = 1
print(r)