l = str(input())
a, b = 0, 0
for i in range(0,len(l),2):
  if l[i]=='A':
    a += int(l[i+1])
  elif l[i]=='B':
    b += int(l[i+1])
  if a==10 and b==10:
    for j in range(i+2,len(l),2):
      if l[j]=='A':
        a += int(l[j+1])
      elif l[j]=='B':
        b += int(l[j+1])
      if a-b>=2:
        print('A')
        break
      elif b-a>=2:
        print('B')
        break
    break
  else:
    if a>=11:
      print('A')
      break
    elif b>=11:
      print('B')
      break