for _ in range(int(input())):
  # 입력
  S = input().lower()

  # 풀이
  s_reversed = ''
  for s in S[::-1]:
    s_reversed += s

  # 출력
  if S==s_reversed:
    print('Yes')
  else:
    print('No')