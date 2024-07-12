while 1:
  # 입력
  N = input()

  # 풀이
  if N=='0':
    break

  while len(N)!=1:
    r = 0
    for n in N:
      r += int(n)
    N = str(r)

  # 출력
  print(N)