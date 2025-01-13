A, B, C, M = map(int, input().split())

a, b = 0, 0
for _ in range(24):
  if a+A<=M:
    a += A
    b += B
  else:
    a -= C
  if a<0: a = 0

print(b)