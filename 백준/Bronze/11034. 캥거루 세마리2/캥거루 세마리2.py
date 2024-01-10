while 1:
  try:
    a, b, c = map(int, input().split())
    r = 0
    while a<b and b<c and not (b-a==1 and c-b==1):
      r += 1
      if b-a>=c-b:
        c = b-1
        c, b = b, c
      else:
        a = b+1
        a, b = b, a
    print(r)
  except:
    break