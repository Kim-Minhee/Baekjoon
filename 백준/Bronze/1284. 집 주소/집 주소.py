while True:
  num = input()
  if num=='0':
    break
  w = 1
  for n in num:
    if n=='1':
      w += 2
    elif n=='0':
      w += 4
    else:
      w += 3
    w += 1
  print(w)