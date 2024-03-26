N = int(input())
for i in range(1, 5*N+1):
  if (i>2*N and i<=3*N) or i>4*N:
    print('@'*5*N)
  else:
    print('@'*N+' '*3*N+'@'*N)