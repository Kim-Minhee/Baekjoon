while True:
  a = list(map(str, input().split()))
  if a==['0', 'W', '0']:
    break
  if a[1]=='W':
    r = int(a[0])-int(a[2])
  else:
    r = int(a[0])+int(a[2])
  if r<-200:
    print('Not allowed')
  else:
    print(r)