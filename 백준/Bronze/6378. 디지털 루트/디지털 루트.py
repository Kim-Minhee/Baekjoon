while 1:
  n = input()
  if n=='0':
    break
  while len(n)!=1:
    r = 0
    for i in n:
      r += int(i)
    n = str(r)
  print(n)