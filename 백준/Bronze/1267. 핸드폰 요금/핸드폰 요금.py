n, time = int(input()), list()
time = list(map(int, input().split()))

y, m = 0, 0
for t in time:
  y += (t//30+1)*10
  m += (t//60+1)*15

if y<m:
  print('Y', y)
elif y>m:
  print('M', m)
else:
  print('Y M', y)