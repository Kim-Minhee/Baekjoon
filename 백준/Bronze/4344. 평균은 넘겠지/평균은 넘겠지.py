c = int(input())
for _ in range(c):
  slist = list(map(int, input().split()))
  hab = sum(slist[1:])
  avg = hab/slist[0]
  cnt = 0
  for i in slist[1:]:
    if i>avg:
      cnt += 1
  print('{:.3f}%'.format(cnt/slist[0]*100))