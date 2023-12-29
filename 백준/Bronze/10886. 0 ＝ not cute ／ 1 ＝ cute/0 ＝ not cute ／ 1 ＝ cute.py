n = c = 0
for _ in range(int(input())):
  v = int(input())
  if v==1:
    c += 1
  else:
    n += 1
if n>c:
  print('Junhee is not cute!')
else:
  print('Junhee is cute!')