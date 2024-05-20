N = int(input())
M = input()
K = int(input())

if M=='annyong':
  if K%2==1:
    print(K)
  else:
    if K-1>0:
      print(K-1)
    else:
      print(K+1)
else:
  if K%2==0:
    print(K)
  else:
    if K-1>0:
      print(K-1)
    else:
      print(K+1)