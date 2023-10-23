t = int(input())
for _ in range(t):
  n = int(input())
  b = str(bin(n))[2:]
  idx = list()
  for i, v in enumerate(b[::-1]):
    if v=='1':
      idx.append(i)
  print(*idx)