p = int(input())
for _ in range(p):
  n, d, a, b, f = map(float, input().split())
  r = (d/(a+b))*f
  print(f'{int(n)} {r:.6f}')