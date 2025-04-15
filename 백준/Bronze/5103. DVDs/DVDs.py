while True:
  CODE = input()
  if CODE=='#': break

  M, S = map(int, input().split())

  for _ in range(int(input())):
    T = input().split()
    if T[0]=='S':
      S -= int(T[1])
      if S<0:
        S = 0
    else:
      S += int(T[1])
      if S>M:
        S = M
  
  print(CODE, S)