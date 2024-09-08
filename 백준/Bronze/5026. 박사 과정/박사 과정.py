for _ in range(int(input())):
  S = input()
  if '=' in S:
    print('skipped')
  else:
    a, b = S.split('+')
    print(int(a)+int(b))