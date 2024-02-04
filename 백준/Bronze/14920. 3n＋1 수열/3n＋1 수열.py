def even(c):
  return c//2

def odd(c):
  return 3*c+1

c, n = int(input()), 1
while c!=1:
  if c%2==0:
    c = even(c)
  else:
    c = odd(c)
  n += 1
print(n)