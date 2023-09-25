t = int(input())
unit = {'kg':[2.2046, 'lb'], 'lb':[0.4536, 'kg'], 'l':[	0.2642, 'g'], 'g':[3.7854, 'l']}
for _ in range(t):
  n, u = map(str, input().split())
  print(f'{round(float(n)*unit[u][0], 4):.4f} {unit[u][1]}')