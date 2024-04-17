for _ in range(int(input())):
  M, KDA, r = int(input()), list(), 0
  for _ in range(M):
    lst = list(map(int, input().split()))
    KDA.append(lst)
  k, d, a = map(int, input().split())
  for i in range(M):
    m = k*KDA[i][0]-d*KDA[i][1]+a*KDA[i][2]
    if m>0:
      r += m
  print(r)