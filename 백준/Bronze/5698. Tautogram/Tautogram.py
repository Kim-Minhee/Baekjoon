while True:
  S = input().lower()
  if S=='*': break

  s_list = S.split()
  start_s = s_list[0][0]
  chk = True
  for s in s_list[1:]:
    if s[0]!=start_s:
      chk = False
      break

  if chk:
    print('Y')
  else:
    print('N')