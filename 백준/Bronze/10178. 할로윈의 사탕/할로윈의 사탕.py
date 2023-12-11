t = int(input())
for _ in range(t):
  c, v = map(int, input().split())
  s, d = c//v, c%v
  print(f'You get {s} piece(s) and your dad gets {d} piece(s).')