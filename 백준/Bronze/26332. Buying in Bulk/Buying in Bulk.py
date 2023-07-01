n =  int(input())
for _ in range(n):
  c, p = map(int, input().split())
  r = c*p
  if c>1:
    r -= (c-1)*2
  print(c, p)
  print(r)