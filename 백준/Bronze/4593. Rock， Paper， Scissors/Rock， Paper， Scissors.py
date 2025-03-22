while True:
  P1, P2 = input(), input()
  if P1==P2=='E': break
  
  p1, p2 = 0, 0
  for i in range(len(P1)):
    if (P1[i]=='R' and P2[i]=='S') or (P1[i]=='S' and P2[i]=='P') or (P1[i]=='P' and P2[i]=='R'):
      p1 += 1
    elif (P2[i]=='R' and P1[i]=='S') or (P2[i]=='S' and P1[i]=='P') or (P2[i]=='P' and P1[i]=='R'):
      p2 += 1
  
  print(f'P1: {p1}')
  print(f'P2: {p2}')