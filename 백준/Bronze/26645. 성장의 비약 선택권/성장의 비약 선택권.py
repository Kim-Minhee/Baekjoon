N = int(input())
if N<210:
  i, j = 1, 1
  m1, m2 = 200, 200
  while i<9 and m1<210:
    m1 = N+i
    i += 1
  while j<5 and m2<220:
    m2 = N+j
    j += 1
  if m1>m2:
    print(1)
  else:
    print(2)
elif N<220:
  i, j = 1, 1
  m1, m2 = 200, 200
  while i<5 and m1<220:
    m1 = N+i
    i += 1
  while j<3 and m2<230:
    m2 = N+j
    j += 1
  if m1>m2:
    print(2)
  else:
    print(3)
elif N<230:
  i, j = 1, 1
  m1, m2 = 200, 200
  while i<3 and m1<230:
    m1 = N+i
    i += 1
  while j<2 and m2<240:
    m2 = N+j
    j += 1
  if m1>m2:
    print(3)
  else:
    print(4)
else:
  print(4)