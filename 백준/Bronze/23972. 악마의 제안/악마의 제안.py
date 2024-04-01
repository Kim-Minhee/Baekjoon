K, N = map(int, input().split())
if N==1:
  print(-1)
else:
  x=K*N//(N-1)
  if (K*N)%(N-1)!=0:
    x += 1
  print(x)