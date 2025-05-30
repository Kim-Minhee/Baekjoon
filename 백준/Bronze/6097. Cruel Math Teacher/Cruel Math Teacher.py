N, P = map(int, input().split())

r = str(N**P)
if len(r)>70:
  for i in range(0, len(r), 70):
    print(r[i:i+70])
else:
  print(r)