import string

a = list(string.ascii_uppercase)

for _ in range(int(input())):
  # 입력
  L, D = map(str, input().split('-'))

  # 풀이
  n = 0
  for i, l in enumerate(reversed(L)):
    n += a.index(l)*(26**i)
  r = abs(n-int(D))

  # 출력
  if r<=100:
    print('nice')
  else:
    print('not nice')