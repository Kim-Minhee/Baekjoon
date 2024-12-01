def convert(num, n):
  if num==0: return 0
  rchar = '0123456789ABCDEF'
  r = ''
  while num>0:
    r += rchar[num%n]
    num //= n
  return r[::-1]

M, N = map(int, input().split())

if N==10:
  print(M)
else:
  print(convert(M, N))