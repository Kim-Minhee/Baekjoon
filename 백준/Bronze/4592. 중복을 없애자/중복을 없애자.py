while 1:

  # 입력
  N = list(map(int, input().split()))
  if N[0]==0:
    break

  # 풀이
  lst = [N[1]]
  for i in range(2, N[0]+1):
    if N[i-1]!=N[i]:
      lst.append(N[i])

  # 출력
  print(*lst, '$')