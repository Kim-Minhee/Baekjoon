def t_n(n):
  t_n = 0
  for i in range(1, n+1):
    t_n += i
  return t_n

t = int(input())
for _ in range(t):
  n, r = int(input()), 0
  for k in range(1, n+1):
    r += k*(t_n(k+1))
  print(r)