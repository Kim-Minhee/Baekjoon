N = int(input())
for i in range(1, 5*N+1):
  if i<=N:
    print('@'*3*N+' '*N+'@'*N)
  elif i>4*N:
    print('@'*N+' '*N+'@'*3*N)
  else:
    print('@'*N+' '*N+'@'*N+' '*N+'@'*N)