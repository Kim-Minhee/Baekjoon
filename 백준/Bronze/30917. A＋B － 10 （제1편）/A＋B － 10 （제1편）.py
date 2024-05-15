chk = False
for a in range(1, 10):
  print('? A', a, flush=True)
  r1 = int(input())
  if r1==1:
    for b in range(1, 10):
      print('? B', b, flush=True)
      r2 = int(input())
      if r2==1:
        print('!', a+b)
        chk = True
        break
  if chk:
    break