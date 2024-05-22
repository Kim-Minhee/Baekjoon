d = {'d1':'q', 'd2':'b', 'b1':'p', 'b2':'d', 'q1':'d', 'q2':'p', 'p1':'b', 'p2':'q'}

N, D = map(str, input().split())
r = list()
for _ in range(int(N)):
  S, a = input(), ''
  for s in S:
    a += d[s+D]
  r.append(a)
for i in range(int(N)):
  print(r[i])