n, f = int(input()), int(input())
if n>5:
  print('Love is open door')
else:
  for _ in range(n-1):
    if f:
      print(0)
      f = 0
    else:
      print(1)
      f = 1