n = int(input())
for i in range(1, n+1):
  a, b, c = map(int, input().split())
  print(f'Scenario #{i}:')
  if (a**2+b**2==c**2)or(b**2+c**2==a**2)or(a**2+c**2==b**2):
    print('yes')
  else:
    print('no')
  if i!=n:
    print()