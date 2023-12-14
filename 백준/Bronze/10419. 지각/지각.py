for _ in range(int(input())):
  d, t = int(input()), 0
  while 1:
    s = t*t
    if t+s>d:
      break
    t += 1
  print(t-1)