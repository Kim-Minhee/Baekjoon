while True:
  n1, n2 = input().split()
  if n1==n2=='0':
    break

  a, b = max(n1, n2), min(n1, n2)
  if len(a)>len(b):
    b = (len(a)-len(b))*'0'+b

  cnt = carry = 0
  for i in range(len(a)-1, -1, -1):
    if int(a[i])+int(b[i])+carry>9:
      cnt +=1
      carry = 1
    else:
      carry = 0
  print(cnt)