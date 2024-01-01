for _ in range(int(input())):
  tc = ts = 0
  for _ in range(int(input())):
    c, g = map(float, input().split())
    tc += int(c)
    ts += c*g
  print(tc, round(ts/tc, 1))