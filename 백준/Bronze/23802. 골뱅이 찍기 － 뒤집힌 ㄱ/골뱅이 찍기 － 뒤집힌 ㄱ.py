N = int(input())
for i in range(5*N):
  if i<=N-1:
    print('@'*5*N)
  else:
    print('@'*N)