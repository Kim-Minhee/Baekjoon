A, c = input(), ''
B = list(map(str, input().split()))
for a in A:
  if a in B:
    c += a.lower()
  else:
    c += a
print(c)