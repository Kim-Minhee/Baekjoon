N, m, M, T, R = map(int, input().split())
if M-m<T:
  print(-1)
else:
  x = m
  i = 0
  while 1:
    i += 1
    if x+T<=M:
      x += T
      N -= 1
      if N==0:
        break
    else:
      x -= R
    if x<m:
      x = m
  print(i)