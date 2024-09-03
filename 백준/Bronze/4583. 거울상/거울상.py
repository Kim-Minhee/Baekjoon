while 1:

  # 입력
  S = input()
  if S=='#':
    break

  # 풀이
  mirror = 'bdpqiovwx'
  change = {'b':'d', 'd':'b', 'p':'q', 'q':'p'}
  r, chk = '', True
  for s in S:
    if s not in mirror:
      chk = False
      break
    if s in 'bdpq':
      r += change[s]
    else:
      r += s
  
  # 출력
  if chk:
    print(r[::-1])
  else:
    print('INVALID')