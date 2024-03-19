A, B, C = map(int, input().split())
m = 0
for _ in range(int(input())):
  s = 0
  for _ in range(3):
    a, b, c = map(int, input().split())
    s += A*a+B*b+C*c
  if s>m:
    m = s
print(m)