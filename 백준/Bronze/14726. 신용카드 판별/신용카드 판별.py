for _ in range(int(input())):
  # 입력
  N = input()[::-1]

  # 풀이
  chk, r = '', 0
  for i, n in enumerate(N):
    if i%2==0: chk += n
    else:
      if int(n)*2<10: chk += str(int(n)*2)
      else: chk += str(int(str(int(n)*2)[0])+int(str(int(n)*2)[1]))
  for c in chk:
    r += int(c)
  
  # 출력
  if r%10==0: print('T')
  else: print('F')