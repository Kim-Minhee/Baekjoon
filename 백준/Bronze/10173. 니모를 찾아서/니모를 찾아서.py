while 1:
  S = input()
  if S=='EOI': break

  if 'nemo' in S.lower():
    print('Found')
  else:
    print('Missing')