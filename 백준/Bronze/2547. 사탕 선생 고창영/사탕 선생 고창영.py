t = int(input())
for _ in range(t):
  input()
  n, s = int(input()), 0
  for _ in range(n):
    c = int(input())
    s += c
  if s%n==0:
    print('YES')
  else:
    print('NO')