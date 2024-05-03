Cu, Du = map(int, input().split())
Cd, Dd = map(int, input().split())
Cp, Dp = map(int, input().split())
H, i = int(input()), 0
while 1:
  if i==0:
    H -= Du
    H -= Dd
    H -= Dp
  else:
    if i%Cu==0:
      H -= Du
    if i%Cd==0:
      H -= Dd
    if i%Cp==0:
      H -= Dp
  if H<=0:
    print(i)
    break
  i += 1