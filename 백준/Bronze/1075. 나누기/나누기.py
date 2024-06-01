N = int(input())
F = int(input())
a = int(str(N)[:-2]+'00')
while 1:
  if a%F==0:
    print(str(a)[-2:])
    break
  else:
    a += 1