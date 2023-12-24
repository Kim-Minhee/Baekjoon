for _ in range(int(input())):
  h, w, n = map(int, input().split())
  for x in range(1, w+1):
    for y in range(1, h+1):
      n -= 1
      if n==0:
        if x<10:
          print(str(y)+'0'+str(x))
        else:
          print(str(y)+str(x))
        break