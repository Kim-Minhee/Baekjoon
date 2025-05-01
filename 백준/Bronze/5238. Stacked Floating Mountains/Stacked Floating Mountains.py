for _ in range(int(input())):
  lst = list(map(int, input().split()))
  k = lst[0]

  chk = True
  for i in range(3, k+1):
    if lst[i-1]+lst[i-2]!=lst[i]:
      chk = False
      break

  print('YES' if chk else 'NO')