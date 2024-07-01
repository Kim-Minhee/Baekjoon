d = {'-':0, '\\':1, '(':2, '@':3, '?':4, '>':5, '&':6, '%':7, '/':-1}

while 1:
  # 입력
  O = input()
  if O=='#':
    break

  # 풀이
  n = 0
  for i, o in enumerate(reversed(O)):
    n += 8**i*d[o]

  # 출력
  print(n)