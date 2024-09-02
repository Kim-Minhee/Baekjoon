for _ in range(int(input())):
  # 입력
  N = input()

  # 풀이
  b, g = N.lower().count('b'), N.lower().count('g')
  r = 'NEUTRAL'
  if b>g:
    r = 'A BADDY'
  elif b<g:
    r = 'GOOD'

  # 출력
  print(f'{N} is {r}')