for _ in range(int(input())):
  r = 0
  for _ in range(int(input())):
    S, R = map(int, input().split())
    r += S*R
  
  print(1296//r, 2592//r, 3888//r)