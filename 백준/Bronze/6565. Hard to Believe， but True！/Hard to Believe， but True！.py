while True:
  E = input()

  a = int(E.split('+')[0][::-1])
  b = int(E.split('+')[1].split('=')[0][::-1])
  c = int(E.split('+')[1].split('=')[1][::-1])
  print(a+b==c)

  if E=='0+0=0': break