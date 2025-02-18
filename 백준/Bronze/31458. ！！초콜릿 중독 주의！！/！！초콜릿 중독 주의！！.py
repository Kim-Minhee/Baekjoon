for _ in range(int(input())):
  a, b = 0, 0
  n = 2
  for t in input():
    if t!='!': n = int(t)
    elif n==2: a += 1
    else: b += 1

  if n==0 and b>0: n = 1
  if a%2!=0 and n==1: n = 0
  elif a%2!=0 and n==0: n = 1

  print(n)