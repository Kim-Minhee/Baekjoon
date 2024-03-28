N = int(input())
for i in range(1, 6):
  if i==1 or i==3:
    for _ in range(N):
      print('@'*5*N)
  else:
    for _ in range(N):
      print('@'*N)