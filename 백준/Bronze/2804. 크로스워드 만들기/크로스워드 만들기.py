a, b = map(str, input().split())
cross = list()
for i in range(len(b)):
  cross.append('.'*len(a))

a_idx, b_idx = int(), int()
for i in a:
  if i in b:
    a_idx = a.index(i)
    b_idx = b.index(i)
    break

cross[b_idx] = a
for i in range(len(b)):
  cross[i] = cross[i][:a_idx]+b[i]+cross[i][a_idx+1:]

for i in cross:
  print(i)