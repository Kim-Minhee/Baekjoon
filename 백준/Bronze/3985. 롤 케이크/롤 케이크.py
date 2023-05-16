l, n = int(input()), int(input())
cake, pk = list(range(1, l+1)), dict()
exp, real = 1, 1
for i in range(1, n+1):
  p, k = list(map(int, input().split()))
  pk[i] = [p, k]
  c = list(range(p, k+1))
  before = len(cake)
  for j in c:
    if j in cake:
      cake.remove(j)
  after = len(cake)
  get = before-after
  pk[i] += [get]
  if (pk[exp][1]-pk[exp][0])<(k-p):
    exp = i
  if pk[real][-1]<get:
    real = i

print(exp)
print(real)