def randnum(num):
  a = str(num**2)
  if len(a)<8:
    a = (8-len(a))*'0'+a
  return int(a[2:6])

while 1:
  A = int(input())
  if A==0: break
  a_set = set([A])
  while 1:
    A = randnum(A)
    a_len = len(a_set)
    a_set.add(A)
    if a_len==len(a_set):
      print(len(a_set))
      break