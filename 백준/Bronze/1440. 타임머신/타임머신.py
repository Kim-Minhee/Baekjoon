D = list(map(int, input().split(':')))
c = list()
for d in D:
  if d>=1 and d<=12:
    c.append(3)
  elif d>=0 and d<=59:
    c.append(2)
  else:
    c.append(0)

if sum(c)==9:
  print(6)
elif sum(c)==8:
  print(4)
elif sum(c)==7:
  print(2)
else:
  print(0)