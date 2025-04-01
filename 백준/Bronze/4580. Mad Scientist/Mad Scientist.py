while True:
  I = list(map(int, input().split()))
  if I==[0]:
    break

  k, p = I[0], I[1:]
  r = [1]*p[0]
  for i in range(1, k):
    temp = [i+1]*(p[i]-p[i-1])
    r.extend(temp)

  print(*r)