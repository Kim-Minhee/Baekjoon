while True:
  X = input()
  if X=='END': break
  else: X = int(X)

  i = 1
  while X!=1:
    X = int(len(str(X)))
    i += 1
  print(i)