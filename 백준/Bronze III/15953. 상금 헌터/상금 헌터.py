def F1(a):
  d, p, t = 1, 1, 1
  while a>t:
    d += 1
    p += 1
    t += p
  return d

def F2(b):
  d, p, t = 1, 1, 1
  while b>t:
    d += 1
    p *= 2
    t += p
  return d

f1, f2 = [500, 300, 200, 50, 30, 10], [512, 256, 128, 64, 32]
for _ in range(int(input())):
  a, b = map(int, input().split())
  m = 0
  if a!=0 and a<=21:
    m += f1[F1(a)-1]
  if b!=0 and b<=31:
    m += f2[F2(b)-1]
  print(m*10000)