num = list(map(int, input().split()))
o = 0
t = 0
for i in num:
  if i==1:
    o += 1
  else:
    t += 1
if o>t:
  print(1)
else:
  print(2)