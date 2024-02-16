for _ in range(int(input())):
  a, b = map(int, input().split())
  d = a//b
  for i in range(1, d):
    d += 2*i
  print(d)