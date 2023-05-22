def change10(b, n):
  l = len(str(n))
  r = 0
  for i in range(l):
    r += int(str(n)[-i-1])*(b**i)
  return r

def changeB(b, n):
  r = ''
  while n>=b:
    r += str(n%b)
    n //= b
  r += str(n)
  return r[::-1]

while True:
  try:
    b, p, m = map(int, input().split())
    p10 = change10(b, p)
    m10 = change10(b, m)
    re = p10%m10
    print(changeB(b, re))
  except:
    break