while True:
  A, B, C, D = map(int, input().split())
  if A+B+C+D==0: break

  a, b, c, d = min(A, B), max(A, B), min(C, D), max(C, D)
  r = 100
  if a>c and b>d:
    r = int(min(c/a, d/b)*100)
  elif a>c:
    r = int(c/a*100)
  elif b>d:
    r = int(d/b*100)
  print(f'{r}%')