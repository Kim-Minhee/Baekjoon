i = 0
while 1:
  I = list(map(int, input().split()))
  if I[0]==0: break
  i += 1
  r, w, l = I[0], I[1], I[2]
  if w**2+l**2<=4*r**2:
    print(f'Pizza {i} fits on the table.')
  else:
    print(f'Pizza {i} does not fit on the table.')