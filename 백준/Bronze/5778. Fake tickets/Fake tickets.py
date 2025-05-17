while True:
  N, M = map(int, input().split())
  if N==M==0: break

  T = list(map(int, input().split()))
  cnt, dupl = 0, []
  for i in range(len(T)):
    t = T[i]
    if t in T[i+1:] and t not in dupl:
      dupl.append(t)
      cnt += 1
  print(cnt)