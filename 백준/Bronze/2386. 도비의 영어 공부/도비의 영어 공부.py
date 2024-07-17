while 1:
  # 입력
  S = list(input().split())

  # 풀이
  if S==['#']:
    break

  a = S[0]
  cnt = 0
  for s in S[1:]:
    for i in s.lower():
      if a==i:
        cnt += 1

  # 출력
  print(a, cnt)