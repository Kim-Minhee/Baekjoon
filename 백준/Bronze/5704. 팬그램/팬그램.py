while 1:
  # 입력
  S = ''.join(input().split())

  # 풀이
  if S=='*': break
  a = [1]*26
  for s in S:
    if a[ord(s)-97]:
      a[ord(s)-97] = 0

  # 출력
  if not sum(a):
    print('Y')
  else:
    print('N')