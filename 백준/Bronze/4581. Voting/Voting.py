while True:
  V = input()
  if V=='#': break
  
  if V.count('A')>=len(V)/2:
    print('need quorum')
  else:
    y, n = V.count('Y'), V.count('N')
    if y==n:
      print('tie')
    elif y>n:
      print('yes')
    else:
      print('no')