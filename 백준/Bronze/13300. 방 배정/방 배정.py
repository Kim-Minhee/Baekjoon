stdt_m, stdt_f = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}, {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
room = 0

N, K = map(int, input().split())
for _ in range(N):
  S, Y = map(int, input().split())
  if S==0:
    stdt_f[Y] += 1
  else:
    stdt_m[Y] += 1

for i in range(1, 7):
  room += stdt_m[i]//K
  room += stdt_f[i]//K
  if stdt_m[i]%K!=0: room += 1
  if stdt_f[i]%K!=0: room += 1

print(room)