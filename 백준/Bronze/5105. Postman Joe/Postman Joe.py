while True:
  D = input().split()
  if D==['#']: break

  non_invited = list(range(1, 21))
  current_floor = int(D[0])
  del non_invited[non_invited.index(current_floor)]

  chk = True
  for d in D[1:]:
    if d[0]=='U':
      current_floor += int(d[1:])
    else:
      current_floor -= int(d[1:])

    if current_floor not in non_invited or current_floor<1 or current_floor>20:
      chk = False
      break
    else:
      del non_invited[non_invited.index(current_floor)]

  if not chk:
    print('illegal')
  elif len(non_invited)==0:
    print('none')
  else:
    print(*non_invited)