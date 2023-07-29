n = int(input())
pepper, t = {'Poblano':1500, 'Mirasol':6000, 'Serrano':15500, 'Cayenne':40000, 'Thai':75000, 'Habanero':125000}, 0
for _ in range(n):
  p = input()
  t += pepper[p]
print(t)