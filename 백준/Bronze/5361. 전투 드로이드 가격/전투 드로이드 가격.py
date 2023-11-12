p = {'a':350.34, 'b':230.90, 'c':190.55, 'd':125.30, 'e':180.90}
t = int(input())
for _ in range(t):
  a, b, c, d, e = map(int, input().split())
  tp = a*p['a']+b*p['b']+c*p['c']+d*p['d']+e*p['e']
  print(f'${tp:.2f}')