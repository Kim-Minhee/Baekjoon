import string

a = list(string.ascii_uppercase)
T = int(input())
for _ in range(T):
  # 입력
  Q, R = input(), input()

  # 풀이
  p = ''
  for q in Q:
    if q==' ':
      p += ' '
    else:
      p += R[a.index(q)]

  # 출력
  print(p)