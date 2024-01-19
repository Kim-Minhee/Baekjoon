l = list()
for i in range(31):
  l.append(2**i)

n = int(input())
if n in l:
  print(1)
else:
  print(0)