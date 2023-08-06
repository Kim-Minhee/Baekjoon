h = 0
for _ in range(4):
  i = list(map(str, input().split()))
  if 'Es' in i:
    h += 21*int(i[-1])
  else:
    h += 17*int(i[-1])
print(h)