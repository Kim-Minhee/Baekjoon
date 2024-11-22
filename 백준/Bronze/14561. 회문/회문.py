def convert(x, n):
  rchar = '0123456789ABCDEF'
  r = ''
  while x>0:
    r += rchar[x%n]
    x //= n
  return r[::-1]

for _ in range(int(input())):
  A, N = map(int, input().split())
  r = str(convert(A, N))
  if r==r[::-1]: print(1)
  else: print(0)