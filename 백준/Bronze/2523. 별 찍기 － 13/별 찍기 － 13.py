n, star = int(input()), list()
for i in range(1, n+1):
  r = '*'*i
  star.append(r)
  print(r)
if len(star)!=1:
  for s in star[n-2::-1]:
    print(s)