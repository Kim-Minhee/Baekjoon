a, b, c = map(int, input().split())
i = 0
while True:
  if (b-a)>=(c-b):
    c = b
    b = a+1
  else:
    a = b
    b = b+1
  if a<b and b<c:
    i += 1
  else:
    break
print(i)