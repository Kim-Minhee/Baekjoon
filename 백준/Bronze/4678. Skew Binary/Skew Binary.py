while True:
  N = input()
  if N=='0':
    break

  l = len(N)
  r = 0
  for i, n in enumerate(N):
    if n!='0':
      r += int(n)*(2**(l-i)-1)

  print(r)