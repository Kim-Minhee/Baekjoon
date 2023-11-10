t = int(input())
for _ in range(t):
  n = int(input())
  p = str()
  for i in range(1, n-1):
    for j in range(i+1, n):
      if i+j==n:
        p += str(i)+' '+str(j)+', '
  print(f'Pairs for {n}:', p[:-2])