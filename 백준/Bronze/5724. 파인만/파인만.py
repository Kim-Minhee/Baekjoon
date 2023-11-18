while 1:
  n, g = int(input()), 0
  if n==0:
    break
  for i in range(n):
    g += (n-i)**2
  print(g)