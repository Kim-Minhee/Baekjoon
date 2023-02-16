t = int(input())
for _ in range(t):
  s = str(input())
  w = 0
  for i in s:
    if i=='U':
      w += 1
    elif i=='D':
      break
  print(w)