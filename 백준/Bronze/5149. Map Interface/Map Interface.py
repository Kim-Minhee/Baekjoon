K = int(input())
for k in range(1, K+1):
  N, M = map(int, input().split())
  STATION = [tuple(map(int, input().split())) for _ in range(N)]
  VISIT = list(map(int, input().split()))

  min_x, max_x, min_y, max_y = int(), int(), int(), int()
  for i, v in enumerate(VISIT):
    x = STATION[v-1][0]
    y = STATION[v-1][1]

    if i==0:
      min_x, max_x = x, x
      min_y, max_y = y, y
    else:
      if x<min_x: min_x = x
      elif x>max_x: max_x = x
      if y<min_y: min_y = y
      elif y>max_y: max_y = y

  cnt = 0
  for s in STATION:
    if min_x<=s[0]<=max_x and min_y<=s[1]<=max_y:
      cnt += 1

  if k!=1: print()
  print(f'Data Set {k}:')
  print(cnt)