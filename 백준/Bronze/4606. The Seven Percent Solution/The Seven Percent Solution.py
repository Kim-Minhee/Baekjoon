encode = {' ':'%20', '!':'%21', '$':'%24', '%':'%25',
          '(':'%28', ')':'%29', '*':'%2a'}

while True:
  S = input()
  if S=='#':
    break

  r = ''
  for s in S:
    if s in encode.keys():
      r += encode[s]
    else:
      r += s

  print(r)