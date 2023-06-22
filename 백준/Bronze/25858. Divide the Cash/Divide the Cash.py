n, d = map(int, input().split())
q, p = [], []

for _ in range(n):
  q.append(int(input()))

for i in q:
  p.append(i*(d//sum(q)))

for i in p:
  print(i)