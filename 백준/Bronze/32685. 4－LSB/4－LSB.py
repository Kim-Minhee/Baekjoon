a = '0b'
for _ in range(3):
  b = bin(int(input()))[2:].zfill(4)
  if len(b)<4:
    b = b.zfill(4)
  a += b[-4:]

r = format(int(a, 2), '04')
print(r)