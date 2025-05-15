while True:
  N, C, K = map(int, input().split())
  if N==C==K==0: break

  cnt = [0]*K
  for _ in range(N):
    X = list(map(int, input().split()))
    for x in X:
      cnt[x-1] += 1

  r = []
  min_cnt = min(cnt)
  for i, c in enumerate(cnt):
    if c==min_cnt:
      r.append(i+1)

  print(*r)