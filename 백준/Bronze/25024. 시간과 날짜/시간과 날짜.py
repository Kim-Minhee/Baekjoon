def time(x, y):
  if x>=0 and x<=23 and y>=0 and y<=59:
    return 'Yes'
  else:
    return 'No'

def date(x, y):
  if (x in [1, 3, 5, 7, 8, 10, 12] and y>=1 and y<=31) or (x in [4, 6, 9, 11] and y>=1 and y<=30) or (x==2 and y>=1 and y<=29):
    return 'Yes'
  else:
    return 'No'

for _ in range(int(input())):
  X, Y = map(int, input().split())
  r1, r2 = time(X, Y), date(X, Y)
  print(r1, r2)