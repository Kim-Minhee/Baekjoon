t = int(input())
for _ in range(t):
  c = int(input())
  cost, r = [25, 10, 5, 1], list()
  for co in cost:
    r.append(int(c//co))
    c %= co
  print(*r)