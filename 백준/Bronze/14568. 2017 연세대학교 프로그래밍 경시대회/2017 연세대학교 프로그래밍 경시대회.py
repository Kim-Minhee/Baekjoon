n, cnt = int(input()), 0
if n>5:
  for a in range(2, n+1, 2):
    for b in range(1, n-a+1):
      if n-a-b>=b+2:
        cnt += 1
  print(cnt)
else:
  print(0)