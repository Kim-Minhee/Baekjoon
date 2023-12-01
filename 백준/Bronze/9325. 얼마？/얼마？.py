t = int(input())
for _ in range(t):
  s, n = int(input()), int(input())
  for _ in range(n):
    q, p = map(int, input().split())
    s += q*p
  print(s)