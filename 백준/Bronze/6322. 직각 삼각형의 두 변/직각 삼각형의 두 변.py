i = 0
while 1:
  a, b, c = map(int, input().split())
  if a==b==c==0:
    break
  i += 1
  if i!=1:
    print()
  if (b==-1 and a>=c-1) or (a==-1 and b>=c-1):
    print(f'Triangle #{i}')
    print('Impossible.')
  else:
    if a==-1:
      s = 'a'
      r = (c**2-b**2)**0.5
    elif b==-1:
      s = 'b'
      r = (c**2-a**2)**0.5
    else:
      s = 'c'
      r = (a**2+b**2)**0.5
    print(f'Triangle #{i}')
    print(f'{s} = {r:.3f}')