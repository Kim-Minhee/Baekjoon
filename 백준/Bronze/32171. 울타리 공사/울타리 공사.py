a, b, c, d = int(), int(), int(), int()

for i in range(int(input())):
  A, B, C, D = map(int, input().split())
  if i==0:
    a, b, c, d = A, B, C, D
  else:
    a, b, c, d = min(a, A), min(b, B), max(c, C), max(d, D)

  print(2*(c-a+d-b))