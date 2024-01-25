t = sorted(list(map(int, input().split())))
if t[0]+t[1]>t[2]:
  print(sum(t))
else:
  print(sum(t[:2])*2-1)