stdt_12, stdt_34m, stdt_34f, stdt_56m, stdt_56f = 0, 0, 0, 0, 0
room = 0

N, K = map(int, input().split())
for _ in range(N):
  S, Y = map(int, input().split())
  if Y<=2: stdt_12 += 1
  elif Y<=4 and S==0: stdt_34f += 1
  elif Y<=4 and S==1: stdt_34m += 1
  elif S==0: stdt_56f += 1
  else: stdt_56m += 1

room += stdt_12//K
room += stdt_34m//K
room += stdt_34f//K
room += stdt_56m//K
room += stdt_56f//K

if stdt_12%K!=0: room += 1
if stdt_34m%K!=0: room += 1
if stdt_34f%K!=0: room += 1
if stdt_56m%K!=0: room += 1
if stdt_56f%K!=0: room += 1

print(room)