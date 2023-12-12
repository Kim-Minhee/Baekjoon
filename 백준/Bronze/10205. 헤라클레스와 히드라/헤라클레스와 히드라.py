k = int(input())
for i in range(k):
  h = int(input())
  for j in input():
    if j=='c':
      h += 1
    else:
      h -= 1
  print(f'Data Set {i+1}:')
  print(h)
  if i!=k-1:
    print()