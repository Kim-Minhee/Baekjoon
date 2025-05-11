while True:
  H = int(input())
  if H==0: break

  r = [H]
  while True:
    hn_1 = r[-1]
    if hn_1==1: break

    if hn_1%2==0:
      r.append(hn_1//2)
    else:
      r.append(3*hn_1+1)

  print(max(r))