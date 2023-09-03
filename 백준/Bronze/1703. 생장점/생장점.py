while True:
  b = list(map(int, input().split()))
  if b == [0]:
    break
  s = 1
  for i in range(1, len(b), 2):
    s = s*b[i]-b[i+1]
  print(s)