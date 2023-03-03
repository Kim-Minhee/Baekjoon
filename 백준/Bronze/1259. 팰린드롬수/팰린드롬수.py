while True:
  s = input()
  if s=='0':
    break
  sr = ''.join(reversed(s))
  if s==sr:
    print('yes')
  else:
    print('no')