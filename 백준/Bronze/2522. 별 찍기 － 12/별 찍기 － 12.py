n, star = int(input()), list()
if n==1:
  print('*')
else:
  for i in range(1, n+1):
    r = ' ' *(n-i)
    r += '*'*i
    star.append(r)
    print(r)
  for s in star[n-2::-1]:
    print(s)