i, r = 1, list()

while 1:
  O, W = map(float, input().split())
  if O==W==0.0:
    break
  
  # 시나리오별 반복
  rip = False
  while 1:
    A, N = map(str, input().split())
    if A=='#':
      break
    elif A=='E':
      W -= int(N)
      if W<=0:
        rip = True
    elif A=='F':
      W += int(N)
  
  # 시나리오 종료 후 펫의 상태
  if rip:
    r.append(str(i)+' RIP')
  elif W>0.5*O and W<2*O:
    r.append(str(i)+' :-)')
  elif W<=0.5*O or W>=2*O:
    r.append(str(i)+' :-(')
  
  i += 1

for i in r:
  print(i)