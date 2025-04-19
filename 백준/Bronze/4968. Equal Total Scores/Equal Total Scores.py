while True:
  N, M = map(int, input().split())
  if N==M==0: break

  taro, hanaco = [], []
  for _ in range(N):
    taro.append(int(input()))
  for _ in range(M):
    hanaco.append(int(input()))
  taro.sort()
  hanaco.sort()

  posible, escape = False, False
  for t in taro:
    for h in hanaco:
      if sum(taro)-t+h==sum(hanaco)-h+t:
        posible = True
        escape = True
        break
    if escape:
      break

  if posible:
    print(t, h)
  else:
    print(-1)