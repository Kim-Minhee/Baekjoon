while 1:
  
  # 입력
  S = input()

  # 풀이
  if S=='0':
    break
  tmp_list = [int(S)]
  while len(S)>1:
    tmp = 1
    for s in S:
      tmp *= int(s)
    tmp_list.append(tmp)
    S = str(tmp)

  # 출력
  print(*tmp_list)