n = int(input())
for n_ in range(n):
  num = list(map(int, input().split()))
  r = ''
  if 17 in num:
    r += 'zack'
  if 18 in num:
    r += 'mack'
  if r=='zackmack':
    r = 'both'
  elif r=='':
    r = 'none'
  print(*num)
  print(r)
  if n_!=(n-1):
    print()