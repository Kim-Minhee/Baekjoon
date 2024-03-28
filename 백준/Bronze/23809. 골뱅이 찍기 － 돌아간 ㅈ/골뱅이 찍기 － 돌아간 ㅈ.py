N = int(input())
for i in range(1, 6):
  if i==1 or i==5:
    for _ in range(N):
      print('@'*N+' '*3*N+'@'*N)
  elif i==2 or i==4:
    for _ in range(N):
      print('@'*N+' '*2*N+'@'*N)
  else:
    for _ in range(N):
      print('@'*3*N)