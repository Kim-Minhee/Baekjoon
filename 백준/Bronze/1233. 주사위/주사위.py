S1, S2, S3 = map(int, input().split())
d = dict()
for i in range(1, S1+1):
  for j in range(1, S2+1):
    for h in range(1, S3+1):
      if i+j+h in d.keys():
        d[i+j+h] += 1
      else:
        d[i+j+h] = 1
m = max(list(d.values()))
for k in d.keys():
  if d[k]==m:
    print(k)
    break