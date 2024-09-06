while 1:

  # 입력
  S = input()
  if S=='#': break

  # 풀이
  cnt = S.count('1')
  if (S[-1]=='e' and cnt%2==0) or (S[-1]=='o' and cnt%2!=0):
    S = S[:-1]+'0'
  else:
    S = S[:-1]+'1'

  # 출력
  print(S)